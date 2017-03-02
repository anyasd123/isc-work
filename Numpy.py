import numpy as np

a = np.array([[2, 3, -5,], [21, -2, 1]])


#dtype to specify decimal points

#start with 0 as with lists and lower limit is inclusive and upper exclusive

#Array Slicing

#rows are first and column second [row, col]

#Exercise 1

import numpy as np
x = range (1, 11)
a1 = np.array(x, np.int32)
a2 =np.array(x, np.float32)
print a1.dtype
print a2.dtype

#Exercise 2

arr = np.zeros((2, 3, 4))
arr = np.ones((2, 3, 4))
arr = np.arrange(1000)

#Exercise 3

a = np.array([[2, 3.2, 5.5, -6.4, -2.2, 2.4],[1, 22, 4, 0.1, 5.3, -9],[3, 1, 2.1, 21, 1.1, -21]])

print a[: ,3]
[-6.4 0.1 21.] #: means top row and then the 3rd (4th) value until the end
print a[1:4, 0:4]
[[1. 22. 4. 0.1]
 [3. 1. 2.1 21.]]
print a[1:, 2]
[4. 2.1]

#See batch job example in parallel processing ppt for CMIP5 and NetCDF. Import cf

n.shape(a)
n.rank(a)
np.size(a)

a.dtype.char #typecode of array
np.reshape(a, (2,3)) #reshape array
np.transpose(a) #transpose array (flipping dimensions) e.g. see exercise 2
np.ravel(a) #flatten a multi dimensional array to a 1D array
np.concatenate(a,b) #sticks one array onto end of another, can specify dimension
np.repeat(a,3) #repeat array elements
b = a.astype

#meshgrid 
#linspace means equally spaced points


#Exercises on interrogating and manipulating arrays

#Exercise 1
arr = np.array([range(4), range(10, 14)])
print arr.shape
print arr.size
print arr.max() #or np.max(arr)
print arr.min() #or np.min(arr)

#Exercise 2
np.reshape(arr, (2, 2, 2))
np.transpose(arr)
np.ravel(arr)
print arr.astype (np.float64)
#often have two ways of doing things with numpy (e.g. see above with min/max)

#np.histogram

#Array calculations and operations exercises

#Exercise 1
a = np.array([range(4), range(10, 14)])
b = np.array([2, -1, 1, 0])
print a * b
b1 = b * 100
b2 = b*100.0
print b2
print b1==b2
print b1.dtype b2.dtype

#Exercise 2
arr = np.arange(10)
#arange is the same as range function but creates an array instead of a list
print arr < 3
print np.less(arr, 3)
condition = np.logical_or(arr < 3 or arr > 8)
new_arr = np.where(condition, arr * 5, arr * -5)

#Exercise 3
def calcMagnitude (u, v, minmag = 0.1:
    mag = ((u**2) + (v**2))**0.5
    output = np.where(mag>minmag, mag, minmag)
return output

u = np.array([[[4, 5, 6], [2, 3, 4]])
v = np.array([[[2, 2, 2], [1, 1, 1]])
print calcMagnitude (u, v)

#Working with missing values exercises

#Exercise 1
import numpy.ma as MA
MARR = MA.masked_array(range (10), fill_value =-999)
print MARR, MARR.fill_value
MARR[2] = MA.masked
print MARR
print MARR.mask

#need to finish from g. 
