from matplotlib.pylab import *

def f(t):
  return t**2*exp(-t**2)

t = linspace(0, 3, 51)  # 51 puntos entre 0 y 3
y = zeros(len(t))       # reserva memoria para y con elementos flotantes
for i in xrange(len(t)):
  y[i] = f(t[i])

plot(t,y)
show()
