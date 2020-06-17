# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit
from scipy.special import factorial


# %%
i=50
j=1
#Read="C:/Users/antoi/Desktop/Vitesse_shunt/"+str(i)+"_"+str(j)+".csv"
Read="railpropre_125_200Hz.csv"
data=pd.read_csv(Read,skiprows=44).values
data


# %%
Volts=data[3:,3]
Time=data[3:,1]
Amps=data[3:,2]
Volts = Volts.astype(np.float)
Time= Time.astype(np.float)
Amps= Amps.astype(np.float)


# %%
#print('Volts ='+'[' +", ".join([str(x) for x in Volts])+']')


# %%
VoltsNorm=(Volts>0.6)*1

# %% [markdown]
# # Statistique 

# %%
plt.figure(figsize=(10,5))
plt.scatter(Time,Volts,linewidth=1)
len(Volts)


# %%
#Volts=Volts[50:900]
#Time=Time[50:900]

# %% [markdown]
# ## Trouver les points où le déshuntage commence

# %%
for i in np.arange(0,len(Volts),1):
    if Volts[i] < 0.2:
        First=i
        break;
        
for i in np.flip(np.arange(0,len(Volts),1)):
    if Volts[i] < 0.2:
        Last=i
        break;


# %%
Volts=Volts[First:Last]
Time=Time[First:Last]
plt.figure(figsize=(10,5))
plt.plot(Time,Volts,linewidth=1)


# %%
Last

# %% [markdown]
# # Plot de la distribution

# %%
Max=np.max(Volts)
Min=0
Pas=0.005
Balayage=np.arange(Min,Max+Pas,Pas)
Balayage


# %%
Nombre=np.zeros(len(Balayage)-1)
VoltsHist=np.zeros(len(Balayage)-1)
for i in np.arange(0,len(Balayage)-1,1):
    A=(Volts>Balayage[i])*1
    B=(Volts<Balayage[i+1])*1
    Nombre[i]=np.sum(A*B)
    VoltsHist[i]=(Balayage[i]+Balayage[i+1])/2


# %%
plt.figure(figsize=(10,5))
plt.plot(VoltsHist,Nombre,linewidth=1)
plt.xlabel('Valeur de la tension (Intervalle de taille '+str(Pas)+')')
plt.ylabel("Nombre de Points dans l'intervalle")

# %% [markdown]
# # Loi de Poisson

# %%
def Poisson(x,a,b,c,d):
    return (1/a)*np.exp(-b*x**2)+c

popt1, pcov1 = curve_fit(Poisson, VoltsHist, Nombre)


# %%

plt.figure(figsize=(10,5))
plt.plot(VoltsHist,Nombre,linewidth=1)
plt.plot(VoltsHist, Poisson(VoltsHist, *popt1),label="Regression")
plt.xlabel('Valeur de la tension (Intervalle de taille '+str(Pas)+')')
plt.ylabel("Nombre de Points dans l'intervalle")

# %% [markdown]
# # Plot de l'histogramme

# %%

Max=np.max(Volts)
Min=0
Pas=0.005
np.sum(A*B)
Balayage=np.arange(Min,Max+Pas,Pas)
Balayage

plt.figure(figsize=(10,5))
plt.hist(Volts,bins=Balayage)

# %% [markdown]
# # Binaire
# 

# %%
from scipy.stats import gamma
from numpy import linspace
from pylab import plot,show,hist,figure,title

# picking 150 of from a normal distrubution
# with mean 0 and standard deviation 1
#samp = gamma.rvs(2,size=1000) 
samp1=Volts
param = gamma.fit(samp1) # distribution fitting

# now, param[0] and param[1] are the mean and 
# the standard deviation of the fitted distribution
x = linspace(0,1,1000)
# fitted distribution
pdf_fitted = gamma.pdf(x,param[0],param[1],param[2])


title('Distribution gamma')
plot(x,pdf_fitted,'r-')
hist(Volts,bins=Balayage,density=True) #density=True #permet de normaliser
show()


# %%
from scipy.stats import  lognorm
from scipy import stats
from numpy import linspace
from pylab import plot,show,hist,figure,title

# picking 150 of from a normal distrubution
# with mean 0 and standard deviation 1
#samp = gamma.rvs(2,size=1000) 
samp1=Volts
param =  lognorm.fit(samp1) # distribution fitting

# now, param[0] and param[1] are the mean and 
# the standard deviation of the fitted distribution
x = linspace(0,1,1000)
# fitted distribution
pdf_fitted =  lognorm.pdf(x,param[0],param[1],param[2])


title('Distribution Weibull')
plot(x,pdf_fitted,'r-')
hist(Volts,bins=Balayage,density=True) #density=True #permet de normaliser
show()


# %%
plt.figure(figsize=(10,5))
plt.plot(Time,Volts,linewidth=1)
plt.plot(Time,VoltsNorm,linewidth=1)


# %%
for i in [50,75,100,125]:
    for j in [1,2]:
        Read="C:/Users/antoi/Desktop/Vitesse_shunt/"+str(i)+"_"+str(j)+".csv"
        data=pd.read_csv(Read,skiprows=44).values
        Volts=data[3:1000,3]
        Time=data[3:1000,1]
        Volts = Volts.astype(np.float)
        Time= Time.astype(np.float)
        plt.figure(figsize=(10,5))
        v=(i*9.42477)/60
        print(v)
        label="Vitesse de"+str(v)+" cm/s"
        plt.plot(Time,Volts,linewidth=1)
        plt.title(label)


# %%



# %%



