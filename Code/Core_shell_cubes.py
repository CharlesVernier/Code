# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 14:24:58 2025

@author: vernier
"""

import matplotlib.pyplot as plt
import numpy as np

# x est le volume d'Ag 100 mM en µL a la puissance 1/3
L0,d0=70,30

x=np.arange(0,10,0.05)
y=[2.15*i**2+0.73*i+d0-L0 for i in x]

for i in range(len(x)):
    if y[i]<0 and y[i+1]>0:
        print("x="+str(x[i]**3))
        print("L="+str(L0+1.67*x[i]+1.35*x[i]**2))
        print("d="+str(d0+2.4*x[i]+3.5*x[i]**2))
        
    