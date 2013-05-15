#!/usr/bin/python
import random, sys
from math import *
from sympy import *

valor_x = Symbol('x')
funcion = cos(pi*valor_x)

def Taylor (funcion,valor_x,c,n):
  
  derivada = diff(funcion,valor_x,n)
  polinomio = ((derivada/(f(n)))*((valor_x - c)**n))
  i=0
  while i<=n:
    print derivada
    print polinomio
    i+=1


if __name__=='__main__':
  
  valor_x=float(sys.argv[1])
  c=float(sys.argv[2])
  n=int(sys.argv[3])

  resultado = eval(str(Taylor (funcion,valor_x,c,n)))
  print resultado
  print "El resultado de evaluar la derivada {0}-esima en el punto {1}, cuyo centro es {2} es {3}".format(n, valor_x, c, eval(str(derivada)))
  



#Derivada



#func = 1/(4*symb_x)
#n = 4

#derivada = diff(func, symb_x, n)
#x = 3.0
#print derivada
#print "El resultado de evaluar la derivada {0}-esima en el punto {1} es {2}".format(n, x, eval(str(derivada)))
