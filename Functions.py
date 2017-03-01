#Define functions using def
#greet is the name of the function and the (_) is the argument e.g. name or number or value or amount 

def greet():
    return 'Good evening, master'

def greet(name)
    answer = 'Hello, ' + name
    return answer

def adjust(value, amount = 2.0):
    return value * amount

def double(x)
    return 2 * x

def threshold(signal):
    return 1.0/ sum(signal)
t = threshold

#Exercise 1
def double_it(number):
    return 2 * number

>>>double_it(4)
8
>>>double_it("hello")
'hellohello'

#Exercise 2
def calc_hypo(a,b):
    hypo = (a**2 + b**2)**0.5
    return hypo
print calc_hypo(3, 4)

#can square root using **0.5 or import numpy and use sqrt

#Exercise 3
def calc_hypo(a,b):
    if type (a) not in (int, float) or type (b) not in (int, float):
        print "Bad Argument" 
        return False
    if type (a) <=0 or type (b) <=0:
        print "Bad Argument"
        return False
    hypo = (a**2 + b**2)**0.5
    return hypo
