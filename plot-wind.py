#!env/bin/python
# vim: set fileencoding=utf-8 :
import sys
import numpy as np
import sqlite3
import pandas as pd
import StringIO
from pandas.io.parsers import read_csv, read_fwf
from pandas.parser import CParserError
import matplotlib; matplotlib.use('Agg')
from matplotlib import cm
from matplotlib import pyplot as plt
from datetime import datetime

import optparse

import windrose

""" Convert from rectangular (x,y) to polar (r,w)
 r = sqrt(x^2 + y^2)
 w = arctan(y/x) = [-\pi,\pi] = [-180,180] 
""" 
def polar(x, y, deg=True): # radian if deg=0; degree if deg=1
   if deg:
      return np.hypot(x, y), 180.0 * np.arctan2(y, x) / np.pi
   else:
      return np.hypot(x, y), np.arctan2(y, x)

def sonic_parse(x):
   #deals with the ^BQ suffix, returns NaN if unparseable
   try:
      return datetime.strptime(x, '%Y-%m-%dT%H:%M:%S.%f \x02Q')
   except ValueError:
      return np.nan

parser = optparse.OptionParser()

parser.add_option("-t", "--title", dest="title", default="Wind Rose", help="Title to appear on output plot")
parser.add_option("-o", "--outfile", dest="outfile", default="windrose.svg", help="Output filename")

(options, files) = parser.parse_args()

sonic = pd.DataFrame()

for f in files:
   if(f[-4:] == '.txt'):# is a CSV output from Gill Windsonic
      try:
         sonic_in = read_csv(f, sep=',', header=None,  names=['DateTimeB','Timezone','DateTime','UGILL','VGILL','Units','Status','Checksum'], engine='c', date_parser=sonic_parse, parse_dates=['DateTime'], index_col='DateTime', error_bad_lines=False)#, dtype={'U': np.float, 'V':np.float})   
         #U and V from the windsonics are not the conventional U and V, correct
         sonic_in.U = -sonic_in.UGILL.convert_objects(convert_numeric=True)
         sonic_in.V = sonic_in.VGILL.convert_objects(convert_numeric=True)
         (sonic_in['speed'],sonic_in['direction']) = polar(sonic_in.U.values,sonic_in.V.values)
      except CParserError:
         print "Error reading " + f
         sonic_in = False
   elif(f[-4:] == '.sdb'):#is a weewx/wview sqlite DB
      con = sqlite3.connect(f)
      sonic_in = pd.read_sql_query('SELECT DATETIME(dateTime,"unixepoch") as DateTime, windDir AS direction, windSpeed * 0.45 AS speed FROM archive', con, parse_dates=['DateTime'], index_col='DateTime')
   
   #append to other data
   if isinstance(sonic_in, pd.DataFrame):
      sonic = pd.concat([sonic,sonic_in])
   
bins = np.arange(0.01,10,1)
ax = windrose.plot_windrose(sonic, kind='bar',bins=bins, lw=1, cmap=cm.Greens, opening=0.8, normed=True )
ax.set_rlabel_position(0)
#ax.set_rgrids([20,40,60,80,100],['20','40','60','80','%'], horizontalalignment='center')
maxr = ax.get_rmax()
#make next-highest multiple of ten
maxr = (np.ceil(maxr/10))*10
radii = np.linspace(0.1, maxr, int(maxr/10) + 1)
radii_labels = [ "%.0f" %r for r in radii ]
radii_labels[0] = "" #Removing label 0
ax.set_rgrids(radii, radii_labels, horizontalalignment='center')
ax.set_thetagrids(ax.theta_angles, labels=['E', 'NE', 'N', 'NW', 'W', 'SW', 'S', 'SE'],frac=1.05)
legend = ax.legend()
legend.set_title(u'Speed / ms¯¹')
#re-do legend to not be rubbish
legend_texts = legend.get_texts()
for i in range(len(bins)-1):
   legend_texts[i].set_text(" %.1f < v < %0.1f" % (bins[i], bins[i+1]))
legend_texts[-1].set_text(" %.1f < v" % bins[-1])

plt.setp(legend_texts, fontsize='x-small')

plt.suptitle(options.title, fontsize=20, y=0.99)
plt.title(sonic.index.min().strftime('%Y-%m-%d') + " to " + sonic.index.max().strftime('%Y-%m-%d'), fontsize=12,y=1.04)
fig = ax.get_figure()
fig.savefig(options.outfile)
