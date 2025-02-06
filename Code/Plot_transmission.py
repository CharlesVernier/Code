# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 14:34:37 2025

@author: vernier
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 18:16:03 2025

@author: charl
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Import libraries
import glob
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

Grandeur_mesurée="Transmittance (%)"
Titre="Ex_24_avant_etching"
Date="\\05_02_2025"
Folder="\\Sample_45_afer_afm"
Selection=[]


# Create the source path 
path = r"\\nas\data\nanolego\Charles Vernier\Postdoc\Charles_microscope\2025"+Date+Folder
# Import files from source folder sorted by creation time with os.path.getctime
csv_files = sorted(glob.glob(path + "\*.csv"),key=os.path.getmtime)

# Read each CSV file into DataFrame
# This creates a list of dataframes
df_list = (pd.read_csv(file,header=None,sep=",") for file in csv_files)

# Concatenate all DataFrames
big_df   = pd.concat(df_list,axis=1, ignore_index=True)


# liste_labels=[file.split(Date+"\\")[1].split(".csv")[0] for file in csv_files]
liste_labels=[]
for i in range(len(csv_files)):
    liste_labels+=[Folder.split("\\")[1]+"_"+str(int(i/2))]

# Plot each spectrum in sepaarate graphs with corresponding title and create list of labels
liste_peaks=[]
for i in range(0,len(big_df.columns),2):
    fig=plt.figure(int(i/2),figsize=[12,12])
    plt.plot(big_df[i],100*big_df[i+1])
    plt.scatter(big_df[i][np.argmax(big_df[i+1]).item()],max(big_df[i+1]),s=12,color="red",label=("T_max="+str(round(max(big_df[i+1]),3)),"Lambda_max="+str(big_df[i][np.argmax(big_df[i+1]).item()])))
    plt.legend(fontsize=20)
    # liste_peaks+=(argrelmin(np.array(100*big_df[i+1]),order=600)[0].tolist())
    # plt.scatter(big_df[i][liste_peaks[i]],big_df[i+1][liste_peaks])
    # liste_labels[int(i/2)]=liste_labels[int(i/2)].split("\\")[0]+"_"+liste_labels[int(i/2)].split("\\")[1]
    plt.title("Sample"+liste_labels[int(i/2)],fontsize=36)
    plt.xlabel('Wavelength (nm)', fontsize=32)
    plt.xticks(fontsize=20)
    plt.ylabel(Grandeur_mesurée, fontsize=32)
    plt.yticks(fontsize=20)

# Plot each spectrum on same graphs with corresponding label
fig_totale=plt.figure(i//2+1,figsize=[12,12])
plt.title(Titre,fontsize=36)
for i in range(0,len(big_df.columns),2):
    plt.plot(big_df[i],100*big_df[i+1],label=liste_labels[int(i/2)])
    # plt.legend(loc="upper right",fontsize=20)
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0,fontsize=16)
    plt.xlabel('Wavelength (nm)', fontsize=32)
    plt.xticks(fontsize=20)
    plt.ylabel(Grandeur_mesurée, fontsize=32)
    plt.yticks(fontsize=20)

# Plot selected spectra on same graphs with corresponding label
# fig_selected=plt.figure(i//2+2,figsize=[12,12])
# plt.title(Titre,fontsize=36)
# for i in Selection:
#     plt.plot(big_df[2*i-2],100*big_df[2*i-1],label=(Folder.split("\\")[1]+"AgNCs_"+str(i)))
#     plt.legend(loc="lower left",fontsize=20)
#     plt.xlabel('Wavelength (nm)', fontsize=32)
#     plt.xticks(fontsize=20)
#     plt.ylabel(Grandeur_mesurée, fontsize=32)
#     plt.yticks(fontsize=20)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    