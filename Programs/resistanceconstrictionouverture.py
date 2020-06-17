import numpy as np
import matplotlib.pyplot as plt
from numba import jit
from scipy.optimize import curve_fit

#LOOP FOR RESISTANCE 

k=0
i=2*np.arange(1,26)
Size=i
Field=np.zeros(len(i))
for HalfSize in i:
    N=100 # Taille du réseau.
    V=np.zeros([N+1,N+1]) #Initialisation du réseau. 
    #V[1:N-1,1:N-1] # V avec une ligne en bas et en haut en moins ainsi que une colonne à gauche et à droite. 
    Eps= 1e-10
    Ecart=1.0
    A=50+HalfSize
    B=50-HalfSize
    while Ecart>Eps:
        Vprec=V.copy()
        V[N,:]=100 # Toutes les colonnes, et la ligne 99
        V[:,0]=V[:,1] #Bord Gauche
        V[:,100]=V[:,99] #Bord Droit 
        V[1:N,1:N]=0.25*(V[2:N+1,1:N]+V[0:N-1,1:N]+V[1:N,2:N+1]+V[1:N,0:N-1])
        V[0,0:B]= V[1,0:B]
        V[0,A:N]= V[1,A:N]
        Ecart = np.max(np.abs(V-Vprec))
    Ey,Ex = np.gradient(V)
    Field[k]=np.sum(Ey[100,:])
    k=k+1

#plt.plot(Size, Field)

def Reg(x, a, b):
    return a/(x**b)

popt1, pcov1 = curve_fit(Reg, Size, Res)
plt.plot(Size, Reg(Size, *popt1),label="Regression")

print(popt1)
Res=100*(1/Field)
plt.plot(Size,Res,linewidth=1,color='k',label="Resistance")
plt.xlabel(r'Ouverture (en %)')
plt.ylabel(r'Resistance (unités arbitraires)')
plt.title("Resistance en fonction de l'ouverture")
plt.legend()