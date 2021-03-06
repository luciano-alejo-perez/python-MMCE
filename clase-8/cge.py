import numpy as np

import sympy as sp


v=sp.Symbol('v')

w=sp.Symbol('w')

y=sp.Symbol('y')

x=sp.Symbol('x')



F=[0.013*v*x+0.023*w*y-v**3, 0.013*v*x+0.023*w*y-w**1.75,
7.5-0.9*v*x+0.17*w*y, 17.5+0.23*v*x-0.6*w*y]  #Resolvemos el Sistema como 0s de esta funcion
JF=sp.Matrix(F).jacobian([v,w,x,y])  #computamos el Jacobiano. Observese el atributo Matrix de sp antes de jacobian

FL=sp.lambdify([v,w,x,y],F)


    #lambdificamos para que sea mas facil evaluar
JFL=sp.lambdify([v,w,x,y],JF)




Y=[2,3,10,8] #un dato inicial cualquiera

for p in range (0,20):                 	#iteracion de newton raphson
	JFp=JFL(Y[0],Y[1],Y[2],Y[3]) #Jacobiano del paso p-esimo
	Fp=FL(Y[0],Y[1],Y[2],Y[3]) #evaluacion de F paso p-esimo
	JFpI=np.linalg.inv(JFp)
	Y=Y-(JFpI.dot(Fp))

print(Y)  #equilibrio
print(FL(Y[0],Y[1],Y[2],Y[3])) #chequeo
