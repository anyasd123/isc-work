#Sets

#Naturally used to find unique items in a collection


letters = set()
for char in 'qawesdhsgh'
   letters.add(char)
print letters


#Methods Operators
#lows.difference(odds) lows - odds
#lows.intersection(odds) lows & odds
#lows.issubset(ten) lows <= ten
#lows < ten
#lows.issuperset(ten)
#lows >= odds
#lows > odds
#lows.symmetric_difference(odds) lows ^ odds
#lows.union(odds) lows | odds

#Exercise 1

set = a([0, 1, 2, 3, 4, 5])
set = b([2, 4, 6, 8])
print a.union(b)
print a.intersection(b)

#Exercise 2
spicegirls = ["mel", "geri", "victoria", "mel", "emma"]
counts ={}
for name in spicegirls:
    if name not in counts:
        counts [name] = 1
    else:
        counts [name] += 1

for name in counts:
    print name, counts[name]

#Exercise 3
if {}:
    print hi

d = {"maggie": "uk", "ronnie": "usa"}


#from NetCdf4 import data
#data = ..

#is-a

    
