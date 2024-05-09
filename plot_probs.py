# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 22:15:00 2024
@author: Amirreza
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import random
import scipy
import geopy


path_loc=r"E:\Foam_Projects\SimulationCase_PhD\ValidCases\CaceC\postProcessing\probes\50\mag(U)"

data=np.genfromtxt(path_loc)

expData=pd.read_excel(r"E:\Foam_Projects\SimulationCase_PhD\ValidCases\CaceC\CaseC(City_blocks).xlsx",sheet_name='result0')
p1=data[:,2]
exp=np.zeros(len(p1))
exp=expData.iloc[2:,7]

yPlus = r"E:\Foam_Projects\SimulationCase_PhD\ValidCases\CaceC\postProcessing\yPlus\0\yPlus.dat"
data_yp= np.genfromtxt(yPlus)

rowCFD=data.shape[0] -1  #row of data - postProcessing probs file
numdata=data[rowCFD,1:]
timeS=data[-1,0]


#numdata_simp=data_simp[rowCFD,1:]
plt.figure(figsize=(12,4), dpi = 600)
plt.title("CFD VS. exp results, normalized velocity" + "Time =" + str (timeS) + "               Avergare Y+ Buildings =" + str(data_yp[-1,-1]))
 
Uref = 2.434 #refrence Velocity at 0.02
normVel = numdata/Uref
plt.plot(normVel,'ko',ls='solid',label = "CFD")

exp = np.array(exp)   
plt.plot(exp,'ro',ls="solid",label =  "CaseC ; Exprimental AIJ case")

   
plt.legend()
    
plt.ylim(0, 3)
plt.xlabel("point No")
plt.ylabel("U/Uz")
plt.xticks(np.arange(0, int(len(exp)) +1 ,10))

plt.figure(figsize=(12,4),dpi = 300)
plt.plot(((normVel - exp) / exp ) * 100 , 'bo',ls='solid',label = "Percentage Error %")
plt.axhline(y=15, color='r', linestyle='dashed')
plt.axhline(y=-15, color='r', linestyle='dashed')

#plt.ylim(-10,10)
#plt.plot(err*100 , label = 'error %')

plt.legend()

"""
    
    

    
#expN=expData.iloc[2:,2]


plt.show()


"""