# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 12:09:19 2023

@author: Charles
"""

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

dAu,dAg=20,60
dtot=dAu+dAg

LAu,LAg=60,20
Ltot=LAu+LAg

nAu,pAu=2,12
nAg,pAg=6,12

N=dAu+dAg
Nx,Ny,Nz=int(dAu/N),int(dAu/N),int(LAu/N)

step=dtot/N

if dAg==0:
    Name="AuNRs"
else:
    Name="AuNRs@Ag"

def Au(x,y,z):
    return abs(((x-dtot/2)/(dAu/2)))**nAu+abs(((y-dtot/2)/(dAu/2)))**nAu+abs(((z-Ltot/2)/(LAu/2)))**pAu

def Ag(x,y,z):
    return abs(((x-dtot/2)/(dtot/2)))**nAg+abs(((y-dtot/2)/(dtot/2)))**nAg+abs(((z-Ltot/2)/(Ltot/2)))**pAg

lAu=[]
lxAu,lyAu,lzAu=[],[],[]
NAu=0
for x in np.arange(0,dtot+step,step):
    for y in np.arange(0,dtot+step,step):
        for z in np.arange(0,Ltot+step,step):
            if Au(x,y,z)<1:
                NAu+=1
                lAu+=[(int(x/step),int(y/step),int(z/step))]
                lxAu+=[x]
                lyAu+=[y]
                lzAu+=[z]
          
Nombre_dipôles=NAu         

lAg=[]
lxAg,lyAg,lzAg=[],[],[]
if dAg!=0:                
    NAg=0 
    for x in np.arange(0,dtot+step,step):
        for y in np.arange(0,dtot+step,step):
            for z in np.arange(0,Ltot+step,step):
                if Ag(x,y,z)<1 and Au(x,y,z)>=1:
                    NAg+=1
                    lAg+=[(int(x/step),int(y/step),int(z/step))]
                    lxAg+=[x]
                    lyAg+=[y]
                    lzAg+=[z]
    Nombre_dipôles=NAu+NAg
                

print("Nombre_de_dipôles=",Nombre_dipôles)
print("aeff=",step*(Nombre_dipôles*3/(4*3.1415))**0.3333)


fig1 = plt.figure(1,figsize=[8,18])
ax = fig1.add_subplot(projection='3d')
ax.scatter(lxAu, lyAu, lzAu,s=1,color="blue")
ax.set_xlim3d(0,dtot+1)
ax.set_ylim3d(0,dtot+1)
ax.set_zlim3d(0,Ltot+1)

plt.show()

if dAg!=0:
    fig2 = plt.figure(2,figsize=[8,18])
    ax = fig2.add_subplot(projection='3d')
    ax.scatter(lxAg, lyAg, lzAg,s=2,color="red")
    ax.set_xlim3d(0,dtot+1)
    ax.set_ylim3d(0,dtot+1)
    ax.set_zlim3d(0,Ltot+1)
    plt.show()

fig3=plt.figure(3,figsize=[8,8])

x=np.arange(0,dtot+1,0.1)
y=np.arange(0,dtot+1,0.1)
xx,yy=np.meshgrid(x,y)
    
valeursAu=abs((xx-dtot/2)/(dAu/2))**nAu+abs((yy-dtot/2)/(dAu/2))**nAu
valeursAg=abs((xx-dtot/2)/(dtot/2))**nAg+abs((yy-dtot/2)/(dtot/2))**nAg


for i in range(len(lAu)):
    if lAu[i][2]==int(Ltot/2):
        plt.scatter(lAu[i][0],lAu[i][1],s=2,color="blue")
        
if dAg!=0:    
    for i in range(len(lAg)):
        if lAg[i][2]==int(Ltot/2):
            plt.scatter(lAg[i][0],lAg[i][1],s=2,color="red")
        

plt.contour(xx,yy,valeursAu,levels=[0.999999999999],colors="blue")
if dAg!=0:
    plt.contour(xx,yy,valeursAg,levels=[0.999999999999],colors="red")

plt.xlim(-1,dtot+1)
plt.ylim(-1,dtot+1)


plt.show()

fig4=plt.figure(4,figsize=[8,8])

x=np.arange(0,dtot+1,0.1)
y=np.arange(0,Ltot+1,0.1)
xx,yy=np.meshgrid(x,y)
    
valeursAu=abs((xx-dtot/2)/(dAu/2))**nAu+abs((yy-Ltot/2)/(LAu/2))**pAu
valeursAg=abs((xx-dtot/2)/(dtot/2))**nAg+abs((yy-Ltot/2)/(Ltot/2))**pAg


for i in range(len(lAu)):
    if lAu[i][0]==int(dtot/2):
        plt.scatter(lAu[i][1],lAu[i][2],s=2,color="blue")
        
if dAg!=0:    
    for i in range(len(lAg)):
        if lAg[i][0]==int(dtot/2):
            plt.scatter(lAg[i][1],lAg[i][2],s=2,color="red")
        

plt.contour(xx,yy,valeursAu,levels=[0.999999999999],colors="blue")
if dAg!=0:
    plt.contour(xx,yy,valeursAg,levels=[0.999999999999],colors="red")

plt.xlim(-1,2*dtot+1)
plt.ylim(-1,Ltot+1)

plt.show()

# textfile = open("%s.txt" % (Name), "w")

# textfile.writelines([">TARREC   rectangular prism; AX,AY,AZ= %s %s %s\n" % (Nx,Ny,Nz),
#                "    %s = NAT\n" % (Nombre_dipôles),
#                "  1.000000  0.000000  0.000000 = A_1 vector\n",
#                "  0.000000  1.000000  0.000000 = A_2 vector\n",
#                "  1 1 1 = lattice spacings (d_x,d_y,d_z)/d\n"
#                " 0 0 0 = lattice offset x0(1-3) = (x_TF,y_TF,z_TF)/d for dipole 0 0 0\n",
#                "    JA IX IY IZ ICOMP(x,y,z)\n"])

# for i in range(len(lAu)+len(lAg)):
#     if i<len(lAu):
#         textfile.write("     {:>6}   {:>2d}   {:>2d} {:>2d} 1 1 1\n".format(i+1,round(lAu[i][0],4),round(lAu[i][1],4),round(lAu[i][2],4)))
#     else:
#         textfile.write("     {:>6d}   {:>2d}   {:>2d} {:>2d} 2 2 2\n".format(i+1,round(lAg[i-len(lAu)][0],4),round(lAg[i-len(lAu)][1],4),round(lAg[i-len(lAu)][2],4)))

# textfile.close()






















