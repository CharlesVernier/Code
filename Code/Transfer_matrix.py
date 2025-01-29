# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 10:01:43 2025

@author: vernier
"""
import numpy as np
import glob
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import argrelmax
from cmath import cos, sin,pi


# Refractive index of the incidence medium
n0=1
# Refractive index of the substrate                   
ns=1
# Thickness of Gold, nm
d=2
# Create the source path 
path= r"\nas\data\nanolego\Charles Vernier\Postdoc\Code\Au_JC_lisse_wavelength_n_k"

file = glob.glob(path + "\*.csv")

# Read each CSV file into DataFrame
# This creates a list of dataframes
df_Au = pd.read_csv(r"\\nas\data\nanolego\Charles Vernier\Postdoc\Code\Au_JC_lisse_wavelength_n_k.csv",header=None,sep=";")

# Wavelengths, n, k
Wavelengths,nAu,kAu=df_Au[0][210:661].to_list(),df_Au[1][210:661].to_list(),df_Au[2][210:661].to_list()

nAu_complexe=[complex(n,k) for (n,k) in zip(nAu,kAu)]

R,T=[],[]

for i in range(len(Wavelengths)):
    k=2*pi/(Wavelengths[i])*nAu_complexe[i]
    M=np.array(([cos(k*d),-1j*sin(k*d)/nAu_complexe[i]] , [-1j*nAu_complexe[i]*sin(k*d),cos(k*d)]))
    r=(M[0][0]*n0 + M[0][1]*n0*ns - M[1][0] - M[1][1]*ns)/(M[0][0]*n0 + M[0][1]*n0*ns + M[1][0] + M[1][1]*ns)
    t=2*n0/(M[0][0]*n0 + M[0][1]*n0*ns + M[1][0] + M[1][1]*ns)
    # La fonction .item() convertit l'affreux np.float en valeur python compréhensible
    R+=[(abs(r).item())**2]
    T+=[(abs(t).item())**2*ns/n0]
    

fig1=plt.figure(1)
plt.plot(Wavelengths,R,label=("d="+str(d)))
plt.title("Reflectance",fontsize=18)
plt.xlabel('Wavelength (nm)', fontsize=18)
plt.xticks(fontsize=16)
plt.ylabel("Reflectance", fontsize=18)
plt.yticks(fontsize=16)
plt.legend()

fig1=plt.figure(2)
plt.plot(Wavelengths,T,label=("d="+str(d)))
plt.scatter(Wavelengths[np.argmax(T).item()],max(T),s=12,color="red",label=("T_max="+str(round(max(T),3)),"Lambda_max="+str(Wavelengths[np.argmax(T).item()])))
plt.title("Transmittance",fontsize=18)
plt.xlabel('Wavelength (nm)', fontsize=18)
plt.xticks(fontsize=16)
plt.ylabel("Transmittance", fontsize=18)
plt.yticks(fontsize=16)
plt.legend()

print("T_max="+str(max(T)))
print("Lambda_max="+str(Wavelengths[np.argmax(T).item()]))


