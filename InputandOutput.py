#Exercise 1
with open ("weather.csv", "r") as reader:
    data = reader.read()
print data

#Exercise 2
with open ("weather.csv") as reader:
    line = reader.readline()
    while line:
        print line
        line = readline()

#Same as saying, keep working through data until data is None (empty)

#Exercise 3
with open ("weather.csv") as reader:
    header = reader.readline()
    rain = []
    for line in reader.readline():
        r = line.strip().split(",")[-1]
        r = float(r)
        rain.append(r)
        
print rain

write (rain) to myrain.txt
