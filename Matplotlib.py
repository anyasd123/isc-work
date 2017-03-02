#Has own interactive plotting window

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.show()
plt.pause(0.1) #may have to do this in order for it to automatically update as window open rather than having to close and open again

'g--'


times = [0, 0.25, 0.5, 0.75]
plt.plot(times, [0,0.5,1,1.2], 'g--',
times, [1, 2, 3, 4], 'r')
plt.ylabel('Concentration (%)')
plt.xlabel('Time (s)')
plt.pause(0.1)

figsize = (10, 10) #size in inches
