import numpy as np
import matplotlib.pyplot as plt
from numba import jit
from scipy.optimize import curve_fit

N=50 # Nombre de ligne 
M=200 # Nombre de colonne 
V=np.zeros([N+1,M+1]) #Initialisation du réseau. 
#V[1:99,1:99]=0.25*(V[2:100,1:99]+V[0:98,1:99]+V[1:99,2:100]+V[1:99,0:98])
#V[1:N-1,1:N-1]=0.25*(V[2:N,1:N-1]+V[0:N-2,1:N-1]+V[1:N-1,2:N]+V[1:N-1,0:N-2])

ParMaille=1#(N/M)**2
Eps= 1e-10
Ecart=1.0
i=np.arange(1,8)
Size=np.zeros(len(i))
Field=np.zeros(len(i))
while Ecart>Eps:
    Vprec=V.copy()
    V[N,:]=100 # Toutes les colonnes, et la ligne 99
    V[:,0]=V[:,1] #Bord Gauche
    V[:,M]=V[:,M-1] #Bord Droit 
    
    V[1:N,1:M]=(1/(2*(ParMaille+1)))*(ParMaille*(V[2:N+1,1:M]+V[0:N-1,1:M])+V[1:N,2:M+1]+V[1:N,0:M-1])
    
    V[0,0:70]= V[1,0:70]
    V[0,130:M]= V[1,130:M]
    Ecart = np.max(np.abs(V-Vprec))

x = np.arange(0,M+1,1)
y = np.arange(0,N+1,1)
X,Y = np.meshgrid(x,y)

A=np.linspace(2,M-2,40)
B = (N-1)*np.ones(len(A))
seed_points = np.array([A,B])


Ey,Ex = np.gradient(V)

Ey=-Ey
Ex=-Ex
%matplotlib inline
plt.rc('text', usetex=False)
plt.rc('font', family='serif')
#1 inch equals to 2.54 cm
fig=plt.figure(figsize=(15/2.54,(9/16)*(15/2.54)))

plt.streamplot(X, Y, Ex, Ey,linewidth=0.75,arrowstyle='->',density=10,start_points=seed_points.T,color="#ef6700")

equ=plt.contour(X,Y,V,10,linewidths=0.7,linestyles="-",colors="k")
plt.clabel(equ, fontsize=7, inline=1,inline_spacing=10,fmt='%1.0f'+" V")

plt.plot([0],[0],label="Equipotentielles",linestyle='-',linewidth=0.9,color="k")
plt.plot([0],[0],label="Ligne de courant",linestyle='-',marker=">",markersize=4,linewidth=0.9,color="#ef6700")
plt.xlabel(r"Nombre de cases selon x",fontsize = 9)
plt.ylabel(r"Nombre de cases selon y",fontsize = 9)
plt.title(r"Résolution du Laplacien sur une matrice $50 \times 200$ ",fontsize = 9,pad=10)
plt.rc('xtick', labelsize=7) 
plt.rc('ytick', labelsize=7) 
plt.legend(prop={'size': 6})