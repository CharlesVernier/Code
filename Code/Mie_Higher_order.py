# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 14:44:29 2024

@author: Charles
"""

from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import numpy as np


r=5
V=4*3.1415*r**3/3
d=2*r

x_old=[187.879,191.654,195.276,199.357,203.279,207.358,211.966,216.405,221.429,
   226.277,231.343,237.094,242.661,248.996,255.144,261.603,268.98,276.169,
   284.404,292.453,300.971,310.777,320.413,331.551,342.541,354.286,367.953,
   381.538,397.436,413.333,430.556,450.909,471.483,496,521.008,548.673,582.16,
   616.915,659.574,704.545,756.098,821.192,892.086,984.127,1087.72,1215.69]

eps1Au=[0.227056,0.295191,0.292524,0.203899,0.138171,-0.010416,-0.1325,-0.233769,-0.346329,-0.4155,-0.551009,-0.616896,-0.744529,
        -0.891261,-1.080444,-1.236501,-1.346409,-1.366509,-1.332261,-1.306784,-1.227421,-1.242549,-1.230804,-1.355289,-1.310241,
        -1.231956,-1.400625,-1.604889,-1.649404,-1.702164,-1.692204,-1.758996,-1.702701,-2.278289,-3.946161,-5.842125,-8.112669,
        -10.661884,-13.648209,-16.817709,-20.610164,-25.811289,-32.040669,-40.2741,-51.0496,-66.218525]

eps2Au=[3.04128,3.17592,3.28568,3.32766,3.39682,3.3904,3.51,3.6062,3.7102,3.8252,3.8922,4.05504,4.16328,4.33846,4.49008,4.7223,
        4.97628,5.28242,5.49486,5.59644,5.78034,5.79258,5.84584,5.57368,5.53816,5.598,5.6092,5.64436,5.73888,5.71736,5.6492,5.28264,
        4.84438,3.81264,2.58044,2.1113,1.66054,1.37424,1.03516,1.06678,1.27176,1.62656,1.92542,2.794,3.861,5.7015]


spl_eps1 = CubicSpline(x_old,eps1Au)
spl_eps2 = CubicSpline(x_old,eps2Au)

x_new=np.linspace(200,1200,501)

eps2=spl_eps2(x_new)
eps1=spl_eps1(x_new)


Qabs,Qsca,Qext=[],[],[]

for i in range(len(x_new)):
    
    x=3.14*d/x_new[i]
    a=1-0.1*x**2*V*(eps1[i]+1.77)
    b=0.1*x**2*V*eps2[i]
    c=1/3+1.77*(eps1[i]-1.77)/((eps1[i]-1.77)**2+eps2[i]**2)-x**2*(eps1[i]+17.7)/30
    d=1.77*eps2[i]/((eps1[i]-1.77)**2+eps2[i]**2)+x**2*eps2[i]/30+4*3.1415**2*2.35*V/(3*x_new[i]**3)
        
    Qabs+=[3.14*r**2*(2*3.1415*1.33/x_new[i])*((a*d-b*c)/(c**2+d**2))]
    Qsca+=[3.14*r**2*(2*3.1415*1.33/x_new[i])**4*(1/(6*3.1415))*((a**2+b**2)/(c**2+d**2))]
    Qext+=[Qabs[i]+Qsca[i]]
 
  

plt.plot(x_new[75:350],Qabs[75:350],"blue",label="Abs")
plt.plot(x_new[75:350],Qsca[75:350],"red",label="Sca")
plt.plot(x_new[75:350],Qext[75:350],"black",label="Ext")
plt.legend(loc="upper right")

print(max(Qext[100:500]))
print(x_new[Qext.index(max(Qext[100:500]))])




# plt.scatter(x_old,eps2Au,s=15,c="black")
# plt.scatter(x_new,eps2,s=0.2,c="red")

















