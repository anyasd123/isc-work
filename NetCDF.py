#NetCDF4-python module

# TO create a netCDF file call Dataset() constructor. This is also method used to open an existing file. 

from netcdf4 import Dataset
dataset = Dataset ('data/test.nc', 'w',format = 'NETCDF4_CLASSIC')
print dataset.file_format

level = dataset.createDimension('level', 10)
lat = dataset.createDimension('lat', 73)
lon = dataset.createDimension('lom', 144)
time = dataset.createDimension('time', None) 

print len(lon)
print time.issunlimited 

#Create variable

import numpy as np
times = dataset.createVariable('time', np.float64, ('time',))etc #time could be large number so float64
#ETC

dataset.description

#Look at NETCDF contents with ncdump
#Can view ncview to see data as graph e.g.
ncview sensor_data.nc

#For a nicer plot use matplotlib
from netCDF import Dataset
import numpy as np

dataFile = 'lalala.nc'

#See PPT for more info 

#Can also plot netcdf data with CIS
