import math
from sympy import *

def f(x):
    return x(x+2)

def f_um(x):
    return math.sqrt(x+1)-1

def f1(n):
    return 2*n

def f2(n):
    return n+3

def conact(f1,f2):
    def f3(x):
        return f1(f2(x))
    return f3

#test   
print(conact(f1,f2)(42) == f1(f2(42)) )