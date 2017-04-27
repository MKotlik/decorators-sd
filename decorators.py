# SoftDev, Decorators Assignment
# Misha Kotlik, James Yang

from time import time
from random import choice

def getBenchmark(f):
    def inner(*args):
        timeInitial = time()
        f(*args)
        return time() - timeInitial
    return inner

def getFuncData(f):
    def inner(*args):
        return "Name: " + f.func_name + "\nArgs: " + str(*args)
    return inner

@getBenchmark
def hello():
    return "Wassup"

@getFuncData
def bark(times, meows):
    return times * meows * "Bark! "

@getBenchmark
def quicksort(l):
    if len(l) <= 1:
        return l
    pivot = choice(l)
    lower = [a for a in l if a < pivot]
    upper = [a for a in l if a > pivot]
    return quicksort(lower) + ([pivot] * l.count(pivot)) + quicksort(upper)

print hello()
print bark(5, 6)
#print quicksort([10,-10,5,201,1234,-343,423,1,17])
#print getBenchmark(quicksort([10,-10,5,201,1234,-343,423,1,17]))
