#!/usr/bin/python

from sympy import *
from math import *

symb_x = Symbol('x')
func = 1/(4*symb_x)
n = 4

derivada = diff(func, symb_x, n)
x = 3.0
print derivada
print "El resultado de evaluar la derivada {0}-esima en el punto {1} es {2}".format(n, x, eval(str(derivada)))
