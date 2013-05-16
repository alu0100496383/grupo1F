from matplotlib.pylab import *
from math import *
from sympy import *


x=linspace(1,2,20)
pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286
sym_c = Symbol('c')
c = 1.5
n = 20


def f1(x):
  funcion = []
  for i in x:
    funcion.append(cos(pi*i))
  return funcion

def fac(n):
  if n == 0:
    return 1 
  else:
    return n * fac(n-1)

def f2(x):
  funcion = cos(pi*sym_c)
  polinomio = []
  for h in x:
    suma = 0
    for i in range(n + 1):
      derivada = eval(str(diff(funcion,sym_c,i)))
      suma += ((derivada/(fac(i)))*((h - c)**i))
    polinomio.append(suma)
  return polinomio

y1 = f1(x)
y2 = f2(x)


p1, = plot(x,y1,'r-')
p2, = plot(x,y2,'bo')
xlabel('Valor de x')
ylabel('Valor de la funcion')
legend([p1, p2], ['Funcion real', 'Inter. Taylor'])
title('Grafico con x variable')
xlim(1.0, 2.0)
show()
