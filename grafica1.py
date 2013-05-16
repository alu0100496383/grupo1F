from matplotlib.pylab import *
from math import *
from sympy import *

x=linspace(-10,10,20)
pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286
funcion = zeros(len(x))
c = 1.25
n = 5

def f1(x):
   for i in xrange(len(x)):
     funcion[i] = cos(pi*(x[i])  
   return funcion

def fac(n):
  if n == 0:
    return 1 
  else:
    return n * fac(n-1)

def f2(x):
  polinomio = 0
  for i in range(n + 1):
    derivada = eval(str(diff(funcion,c,i)))
    polinomio += ((derivada/(fac(i)))*((x - c)**i))
  return polinomio


y1 = f1(x)
y2 = f2(x)

plot(x,y1,'r-')
hold('on')
plot(x,y2,'bo')
xlabel('valor de x')
ylabel('valor de la funcion')
legend(['funcion real', 'Taylor'])
title('Grafico con x variable')
show()
