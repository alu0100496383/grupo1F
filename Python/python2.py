#!/usr/bin/python 
import random, sys
from sympy import *

valor_c = Symbol('c')
pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286
funcion = cos(pi*valor_c)

def fac(n):
  if n == 0:
    return 1 
  else:
    return n * fac(n-1)

def Taylor(x,c,n):
  polinomio = 0
  for i in range(n + 1):
    derivada = eval(str(diff(funcion,valor_c,i)))
    polinomio += ((derivada/(fac(i)))*((x - c)**i))
  return polinomio

def real(x):
  resultado = eval(str(cos (pi*x)))
  return resultado

if __name__=='__main__': 
  x=float(sys.argv[1])
  c=float(sys.argv[2])
  n=int(sys.argv[3])
  print "El resultado de evaluar la derivada {0}-esima en el punto {1}, cuyo centro es {2} es {3}".format(n, x, c, Taylor(x,c,n))
  print "El valor real de la funcion en el punto {0} es: {1}".format(x, real(x))
  print "El error es ", abs(real(x)-Taylor(x,c,n))
