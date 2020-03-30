# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 14:34:58 2020

@author: enes_
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


varr2=pd.DataFrame()
varr1=pd.DataFrame()
meanvar11 = pd.DataFrame()
meanvar22 = pd.DataFrame()

for i in range(0,50):
    varr2[i]=np.random.normal(-1, 1, 1000)
    
meanvar2 = pd.DataFrame(varr2.mean())

    
for i in range(0,1000):
    varr1[i]=(np.random.normal(1, 2, 1000))

    
meanvar1 = pd.DataFrame(varr1.mean())

for i in range(1,len(meanvar1)):
    
    meanvar11[i] = (meanvar1[0:i].sum())/i

for i in range(1,len(meanvar2)):
    
    meanvar22[i] = (meanvar2[0:i].sum())/i
    
    
meanvar22= -np.transpose(meanvar22)
meanvar11= np.transpose(meanvar11)

plt.figure()
plt.subplot(121)
plt.plot(meanvar22)
plt.hlines(1, 0, 50, colors= 'r' )
plt.subplot(122)
plt.plot(meanvar11)
plt.hlines(1, 0, 1000, colors= 'r' )
    

    
