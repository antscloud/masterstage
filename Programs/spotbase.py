import numpy as np
import matplotlib.pyplot as plt
from numba import jit
from scipy.optimize import curve_fit

N=100 # Taille du réseau.
V=np.zeros([N+1,N+1]) #Initialisation du réseau. 
#V[1:99,1:99]=0.25*(V[2:100,1:99]+V[0:98,1:99]+V[1:99,2:100]+V[1:99,0:98])
#V[1:N-1,1:N-1]=0.25*(V[2:N,1:N-1]+V[0:N-2,1:N-1]+V[1:N-1,2:N]+V[1:N-1,0:N-2])

N=100 # Taille du réseau.
V=np.zeros([N+1,N+1]) #Initialisation du réseau. 
V[1:N-1,1:N-1] # V avec une ligne en bas et en haut en moins ainsi que une colonne à gauche et à droite. 

Eps= 1e-10
Ecart=1.0
i=np.arange(1,8)
Size=np.zeros(len(i))
Field=np.zeros(len(i))
while Ecart>Eps:
    Vprec=V.copy()
    V[N,:]=100 # Toutes les colonnes, et la ligne 99
    V[:,0]=V[:,1] #Bord Gauche
    V[:,100]=V[:,99] #Bord Droit 
    V[1:N,1:N]=0.25*(V[2:N+1,1:N]+V[0:N-1,1:N]+V[1:N,2:N+1]+V[1:N,0:N-1])
    V[0,0:45]= V[1,0:45]
    V[0,55:N]= V[1,55:N]
    Ecart = np.max(np.abs(V-Vprec))


x = np.arange(0,N+1,1)
y = np.arange(0,N+1,1)
X,Y = np.meshgrid(x,y)

A=np.linspace(0,N,40)
B = 75*np.ones(len(A))
seed_points = np.array([A,B])


Ey,Ex = np.gradient(V)

Ey=-Ey
Ex=-Ex
plt.figure(figsize=(8,5))
plt.contour(X,Y,V,20,colors='b')
plt.streamplot(X, Y, Ex, Ey,linewidth=1,arrowstyle='->',density=10,start_points=seed_points.T,color='orange')
plt.show()

print(np.sum(Ey[100,:]))