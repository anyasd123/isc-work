mylist = [23, "hi", 2.4e-10]
count = 0
while count < 3:
    item = mylist[count]
    print item, mylist.index (item)
    count += 1


x = 1
if x:
    print x, "is True"

if 22.1: 
    print 22.1, "is True"

if "hello":
    print "hello", "is True"

if [1, 2]:
    print [1, 2], "is True"

if 0: 
    print "True"

if 0.0:
    print "True"

if None: print "True"

if False: print "True"
