#Index from 0 not 1

gases = ['He', 'Br', 'Cl']
    print 2
Cl

print len(gases)
2

print gases.count('Br')
2

gases.sort ()
print gases
['Br', 'Cl', 'He']

gases.reverse
print gases
['He', 'Cl', 'Br']

#Range will assume starting at 0 unless otherwise specified and will end at the length of the list -1

print range(5)
[0, 1, 2, 3, 4,]

print range(2, 6)
[2, 3, 4, 5]

#Exercise 1
mylist = [1, 2, 3, 4, 5]
print mylist [1]
print mylist [1:]
print mylist [1:-1] 
print mylist [:]
print mylist [1:4]

#Exercise 2
one_to_ten = range(1, 11)
one_to_ten[0] = 10
one_to_ten.append(11)
one_to_ten.extend([12, 13, 14])

#Exercise 3
forward = []
backward = []
values = ["a", "b", "c"]
for item in values: 
    forward.append(item)
    backward.insert(0, item)
print forward
print backward 

#Exercise 4
countries = ["uk", "usa", "uk", "uae"]
dir(countries)
help(countries.count)
countries.count("uk")
     

#Lists are heterogenous (not every value must be of same type)
#Can loop over elements to "do all" 
#Can use while to step through all possible indices

#Appending values to a list lengthens it

#Slicing
element = 'uranium'
print element [1:4]
>>ran
#Strings are lists of characters.. Can use [] to get 5th character from list [4]
#As with range function, slicing is inclusive of element at bottom and exclusive at top

#Aliasing
