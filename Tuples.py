#An immutable and heterogenous sequence
#Dont need parantheses if context is enough
#Item is temporary variable that takes on value in loop until loop is complete

colours = ['yellow', 'magenta', 'lavender']
left, middle, right = colours
print left, middle, right

pairs = [(1, 10), (2, 20), (3, 30), (4, 40)]
for (low, high) in pairs:
print low + high

#Exercise 1

t = (1,)
print t[-1]
tulip = range(100, 201)
tup = tuple(tulip)
print tup [0], tup [-1]

#Exercise 2
mylist = [23, "hi", 2.4e-10]
for (count, item) in enumerate(mylist):
    print count, item

#Exercise 3
first, middle, last = mylist
print first, middle, last
(first, middle, last) = (middle, last, first)
print middle, last, first
