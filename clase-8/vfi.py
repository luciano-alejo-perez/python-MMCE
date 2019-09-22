import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate

c=sp.Symbol('c')  #simbolo, consumo
k=sp.Symbol('k')  #simbolo, capital

us=sp.log(c) #Funcion de Utilidad - version sympy
fs=sp.sqrt(k) #Funcion de Produccion - version sympy

u=sp.lambdify(c,us) #Funcion de Utilidad - version Lambda
f=sp.lambdify(k,fs) #Funcion de Utilidad - version Lambda

V0=np.zeros(200) #Inicializa V0 para las iteraciones

V1=np.zeros(200) #Inicializa V1 para las iteraciones

g=np.zeros(200) #Inicializa g, funcion politica

K=np.linspace(0.11,0.22,200) #Malla para K. Valores cerca de K*

for i in range(0,200):
	V0[i]=u(f(K[i]))  #Primera iteracion de V

for i in range(0,200):    #Segunda Iteracion de V
	m=np.zeros(200)
	for j in range (0,200):
		m[j]=u(f(K[i])-K[j])+0.9*V0[j]
	M=max(m)
	V1[i]=M

er=np.linalg.norm(V1-V0,np.inf) #Distancia entre las dos iteraciones V0 y V1 

z=1 #Solo un contador para las iteraciones, optativo


while er>0.1: #Iteracion completa
	z=z+1
	V0=V1 #Cambiamos V0 por el siguiente
	V1=np.zeros(200) #Borramos V1 para hacer el nuevo
	for i in range(0,200): #Iteramos lo anterior
		m=np.zeros(200)
		for j in range (0,200):
			m[j]=u(f(K[i])-K[j])+0.9*V0[j]
		M=max(m)
		t=np.argmax(m)
		V1[i]=M
		g[i]=K[t] #Almacenamos la funcion politica
	er=np.linalg.norm(V1-V0,np.inf) #calculamos la distancia de nuevo


import scipy.interpolate
g_in=scipy.interpolate.interp1d(K,g) #Armamos la funcion politica interpolando

T=range(100) #El T para la trayectoria

tray=np.zeros(100) #Inicializa vector tray

tray[0]=0.12 #Elegimos un K0, e.g. K0=0.12

for l in range(0,99):
	tray[l+1]=g_in(tray[l]) #La trayectoria es K_t+1=g(K_t)

plt.figure()
plt.subplot(311)
plt.plot(K,V1)
plt.title('Funcion Valor')

plt.subplots_adjust(hspace=0.6)

plt.subplot(312)
plt.plot(K,g)
plt.title('Funcion Politica')

plt.subplots_adjust(hspace=0.6)

plt.subplot(313)
plt.plot(T,tray)
plt.title('Trayectoria de Acumulacion de K')

plt.show()
