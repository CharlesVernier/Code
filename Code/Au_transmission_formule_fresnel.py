# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 14:41:52 2025

@author: vernier
"""

# This code solves a multilayer system using the Transfer Matrix Method, for
# an angle of incidence of 0 degrees with respect to the surface normal,
# and for the specific case of Periodic bilayer (Bragg Mirror)
# Implemented by Beniamino Sciacca, beni.sciacca@gmail.com

import numpy as np
import glob
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import argrelmax
from cmath import cos, sin,pi

Grandeur_mesurée="Transmittance (%)"
Titre="Sample ex_22 after overnight etching"
Date="\\22_01_2025"
Folder="\\Ex_22_etching_overnight"
Selection=[]

# Refractive index of the incidence medium
n0=1
# Refractive index of the substrate                   
ns=1
# Thickness of Gold, nm
d=1

# Create the source path 
path= r"\nas\data\nanolego\Charles Vernier\Postdoc\Code_\Au_JC_lisse_wavelength_n_k"

file = glob.glob(path + "\*.csv")

# Read each CSV file into DataFrame
# This creates a list of dataframes
df_Au = pd.read_csv(r"\\nas\data\nanolego\Charles Vernier\Postdoc\Code_\Au_JC_lisse_wavelength_n_k.csv",header=None,sep=";")

# Wavelengths, n, k
Wavelengths,nAu,kAu=df_Au[0][210:461].to_list(),df_Au[1][210:461].to_list(),df_Au[2][210:461].to_list()

nAu_complexe=[complex(n,k) for (n,k) in zip(nAu,kAu)]

# Absorption coeff from chapter 1 Mark Fox
absorption_coeff=[4*3.1415*k/w for (k,w) in zip(kAu,Wavelengths)]

# Absorption coeff from chapter 7 Mark Fox
absorption_coeff=[4*3.1415*k/w for (n,k,w) in zip(nAu,kAu,Wavelengths)]

# R_air_Au=[(abs((n-n0)/(n+n0)))**2 for n in nAu_complexe]
# R_Au_verre=[(abs((n-ns)/(n+ns)))**2 for n in nAu_complexe]

R_air_Au=[((n-n0)**2+k**2)/((n+n0)**2+k**2) for (n,k) in zip(nAu,kAu)]
R_Au_verre=[((n-ns)**2+k**2)/((n+ns)**2+k**2) for (n,k) in zip(nAu,kAu)]

T=[(((1-R1)*(1-R2)*2.718**(-alpha*d))/(1-cos(2*R1*2*d*pi*n*2.718**(-alpha*d)/w)+R1*R2*2.718**(-2*alpha*d)))
   for (R1,R2,alpha,n,w) in zip(R_air_Au,R_Au_verre,absorption_coeff,nAu_complexe,Wavelengths)]


fig1=plt.figure(1)
plt.plot(Wavelengths,T,label=("d="+str(d)))
plt.legend()

# Plot de n et k

# fig2=plt.figure(2)
# plt.plot(df_Au[0],df_Au[1],label="n_Au")
# plt.scatter(Wavelengths,nAu,s=0.8,color="Red")
# plt.legend()

# fig3=plt.figure(3)
# plt.plot(df_Au[0],df_Au[2],label="k_Au")
# plt.scatter(Wavelengths,kAu,s=0.8,color="Red")
# plt.legend()
    
    




# # Refractive index of the incidence medium
# n0=1;
# # Refractive index of layer 2                
# n2=1.5      
# # Refractive index of layer 1            
# n1=1.7
# # Refractive index of the substrate                   
# ns=1.51
# # Thickness of layer 1 (nm)              
# d1=100
# # Thickness of layer 2 (nm)                  
# # d2=200
# # Number of repetitions of the bilayer                 
# # N=10         

# R,T=[],[]

# for i in range(len(W)):
#     #k1 et k2 en rad*nm^-1
#     k1=2*3.1415/W[i]*n1
#     k2=2*3.1415/W[i]*n2
#     M1=[cos(k1*d1) -i*sin(k1*d1)/n1 , -i*n1*sin(k1*d1) cos(k1*d1) ]
#     M2=[cos(k2*d2) -i*sin(k2*d2)/n2 , -i*n2*sin(k2*d2) cos(k2*d2) ]
#     # M=(M1*M2)^N
#     # Reflection coefficient
#     r=(M(1,1)*n0 + M(1,2)*n0*ns - M(2,1) - M(2,2)*ns)/(M(1,1)*n0 + M(1,2)*n0*ns + M(2,1) + M(2,2)*ns)
#     # Transmission coefficient
#     t=(M(1,1)*n0 + M(1,2)*n0*ns - M(2,1) - M(2,2)*ns)/(M(1,1)*n0 + M(1,2)*n0*ns + M(2,1) + M(2,2)*ns)
#     # Reflectivity
#     R+=abs(r)^2
#     # Transmissivity
#     T+=abs(t)^2
    
    
    