import numpy as np
import matplotlib.pyplot as plt
from numba import jit
from scipy.optimize import curve_fit


## Il faut encore faire le bon pas, ie la distance entre les trous dans l'algorithme 


N=2 # Nombre de ligne 
M=240 # Nombre de colonne
Scale=2 #Taille du spot 
Shift=np.arange(0,int(M/(2*Scale)),1) # le -1 permet d'éviter le trou au milieu 
# Facteur qui Permet de calculer le décalage des spots, à mettre en relation avec les conditions aux limites
# 

EyInfluenceTot=np.zeros(len(Shift))
EyInfluenceTrou1=np.zeros(len(Shift))
EyInfluenceTrou2=np.zeros(len(Shift))

k=0

for n in Shift:
    N=2 # Nombre de ligne 
    M=240 # Nombre de colonne 
    V=np.zeros([N+1,M+1]) #Initialisation du réseau. 
    ParMaille=1#(N/M)**2
    Eps= 1e-10
    Ecart=1.0
    i=np.arange(1,8)
    Size=np.zeros(len(i))
    Field=np.zeros(len(i))
    while Ecart>Eps:
        Vprec=V.copy()
        V[N,:]=100 # Toutes les colonnes, et la plus haute ligne
        V[:,0]=V[:,1] #Bord Gauche
        V[:,M]=V[:,M-1] #Bord Droit 

        V[1:N,1:M]=(1/(2*(ParMaille+1)))*(ParMaille*(V[2:N+1,1:M]+V[0:N-1,1:M])+V[1:N,2:M+1]+V[1:N,0:M-1])

        #Conditions sur les plaques 
        V[0,0:(0+n*Scale)]= V[1,0:(0+n*Scale)] # n doit commencer à 1 #Feuille avec calculs 
        V[0,(Scale+n*Scale):(M-Scale-n*Scale)]= V[1,(Scale+n*Scale):(M-Scale-n*Scale)]
        V[0,(M-n*Scale):M]= V[1,(M-n*Scale):M]
        #Critère de convergence 
        Ecart = np.max(np.abs(V-Vprec))
    Ey,Ex = np.gradient(V)
    EyInfluenceTot[k]=np.sum(Ey[N,:])
    EyInfluenceTrou1[k]=np.sum(Ey[0,n*Scale:(n+1)*Scale])
    EyInfluenceTrou2[k]=np.sum(Ey[0,M-(n+1)*Scale:M-n*Scale])
    k=k+1

Res=100/(EyInfluenceTrou1+EyInfluenceTrou2)
plt.plot(Shift,Res)
plt.xlabel("Distance entre les spots")
plt.ylabel("Resistance")
plt.title("Test indépendance")