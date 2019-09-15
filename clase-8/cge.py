import numpy as np
import sympy as sp

v=sp.Symbol('v')
w=sp.Symbol('w')
y=sp.Symbol('y')
x=sp.Symbol('x')

F=sp.matrix([0.013*v*x+0.023*w*y-v**3, 0.013*v*x+0.023*w*y-w**1.75,
7.5-0.9*v*x+0.17*w*y, 17.5+0.23*v*x-0.6*w*y])

FL=lambdify([v,w,x,y],F)


