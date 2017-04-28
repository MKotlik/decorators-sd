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
        s = "Name: " + f.func_name + "\nArgs: "
        for arg in args:
            s += str(arg) + ", "
        return s[:-2]
    return inner

@getBenchmark
def hello():
    return "Wassup"

@getFuncData
def bark(times, meows):
    return times * meows * "Bark! "

@getBenchmark
def quicksortWrapper(l):
    def quicksort():
        if len(l) <= 1:
            return l
        pivot = choice(l)
        lower = [a for a in l if a < pivot]
        upper = [a for a in l if a > pivot]
        return quicksort(lower) + ([pivot] * l.count(pivot)) + quicksort(upper)
    return quicksort
print hello()
print bark(5, 6, 5)
print quicksortWrapper([10,-10,5,201,1234,-343,423,1,17])
#print getBenchmark(quicksort([10,-10,5,201,1234,-343,423,1,17]))
