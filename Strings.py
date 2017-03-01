name = 'Darwin'
for c in name:
    print c

#Strings are immutable (cannot append to it etc)

name = 'Darwin'
name[0] = 'C'
#Type Error

name = 'Charles' + ' ' + 'Darwin
print name

#Concatenation
original = 'Charles'
name = original
name += 'Darwin'

#Accessing arguments by position using formatting method
'{0}, {1}, {2}'.format('a', 'b', 'c')

'a, b, c'

'{}, {}, {}'.format('a', 'b', 'c') # Py2.7+

'a, b, c'

'{2}, {1}, {0}'.format('a', 'b', 'c')

'c, b, a'

#Accessing arguments by name
'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')

'Coordinates: 37.24N, -115.81W'


percentage_yield = 12.3
print 'yield: {:6.2f}'.format(percentage_yield)

print 'There isn\'t time\nto do it right'

name = 'newTON'
print name.capitalize(), name.upper(), name.lower(), name


dna = 'acggtggtcac'
print dna.count('g'), dna.count('x')

print dna.find('t'), dna.find('t', 5), dna.find('x')
#Find uses 0 as 1... 0 also means false so that is why -1 is printed with dna.find('x')
print dna.replace('t', 'x')

print dna.replace('gt', '')

element = 'celsium'
print element.upper().center(10, '.')

#Regular expressions - for advanced string/text processing. 
#Use "re" library in Python

#Exercise 1
s = "I love to write python"
for i in s:
    print i
print s[4]
print s[-1] 
print len(s)

#Exercise 2
split_s = s.split (",")
for word in split_s:
    if word.find("i"): 
       print "I found ",i," in:", word

#[]: Used to define mutable data types - lists, list comprehensions and for indexing/lookup/slicing.
#(): Define tuples, order of operations, generator expressions, function calls and other syntax.
#{}: The two hash table types - dictionaries and sets.



#Exercise 3
something = "Completely Different"
print dir(something)
something.count('t')
something.find ('plete')
something.split ("e")
thing2 = something.replace ("Different", "Silly")
something[0] = "B" #This does not work as strings are immutable so cannot be changed!

#.strip will get rid of white space 
