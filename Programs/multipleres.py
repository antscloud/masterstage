import numpy as np
import matplotlib.pyplot as plt
from numba import jit
from scipy.optimize import curve_fit

k=0
i=4*np.arange(1,26)
Size=2*i
Field=np.zeros(len(i))
Height=np.flip(np.arange(5,100,10))
AllField=np.zeros([len(Height),len(Field)])

y=0
for N in Height:
    k=0
    i=4*np.arange(1,26)
    Size=2*i
    Field=np.zeros(len(i))
    for HalfSize in i:
        #N=5 # Nombre de ligne 
        M=200 # Nombre de colonne 
        V=np.zeros([N+1,M+1]) #Initialisation du réseau. 

        ParMaille=1#(N/M)**2
        Eps= 1e-10
        Ecart=1.0
        while Ecart>Eps:
            Vprec=V.copy()
            V[N,:]=100 # Toutes les colonnes, et la ligne 99
            V[:,0]=V[:,1] #Bord Gauche
            V[:,M]=V[:,M-1] #Bord Droit 

            V[1:N,1:M]=(1/(2*(ParMaille+1)))*(ParMaille*(V[2:N+1,1:M]+V[0:N-1,1:M])+V[1:N,2:M+1]+V[1:N,0:M-1])

            V[0,0:(100-HalfSize)]= V[1,0:(100-HalfSize)]
            V[0,(100+HalfSize):M]= V[1,(100+HalfSize):M]
            Ecart = np.max(np.abs(V-Vprec))

        Ey,Ex = np.gradient(V)
        Field[k]=np.sum(Ey[0,(100-HalfSize):(100+HalfSize)])
        k=k+1
    AllField[y]=Field
    y=y+1

FigAllRes=plt.figure(figsize=(15/2.54,(9/16)*(15/2.54)))
#def Reg(x, a, b):
#    return a/(x) 

#ResReg=100/AllField[9]

#popt1, pcov1 = curve_fit(Reg, Size, ResReg)

#Axis=np.arange(3,200,1)
#Regression=popt1[0]/Axis
#plt.plot(Axis, Regression,color="grey",label="Regression")
plt.rc('text', usetex=False)
plt.rc('font', family='serif')

styl_list=['-','--','-.',':']
marker_list_full=['.', ',' ,'o','v','^','<','>','1','2','3','4','s','p','*','h','H','+','x','D','d','|','_']
marker_list=['o','v','^','<','>','s','p','*','h','H','+','x','D','d','|','_']
for i in np.arange(10):
    styl=styl_list[i %4]
    mark=marker_list[i]
    Res=100/AllField[i]
    plt.plot(Size,Res,label="M="+str(int(Height[i])),marker=mark,linewidth=0.8,markersize=3)
plt.ylim([0,1.2])
plt.legend()

plt.annotate("     Distance \n Surface/Spot",
            xy=(10, 0.1), xycoords='data', fontsize=7,
            xytext=(75, 1), textcoords='data',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"),
            )
plt.xlabel(r'Diamètre du spot',fontsize=9)
plt.ylabel(r'Resistance (unités arbitraires)',fontsize=9)
plt.title(r"Resistance en fonction de l'ouverture pour une matrice $M\times 200$",fontsize=9)
plt.legend(prop={'size': 6})