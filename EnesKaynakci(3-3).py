# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 14:34:59 2020

@author: enes_
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



dagilim = np.random.normal(5,0.1,10000)

plt.subplot(1,2,1)
plt.hist(dagilim, bins = 50 )

std_norm = np.random.normal(0, 1, 10000)

dagilim.sort()
std_norm.sort()


plt.figure(figsize=(8,5), dpi = 100)
plt.plot(std_norm, dagilim, "o") 
plt.ylabel('Normal Dağılım') 
plt.xlabel('Standart Normal Dağılım')


plt.show()


















df = pd.DataFrame()

df =pd.read_csv("GOOG.csv")

df = df["Open"]

getiri = list()

for i in range(1,len(df)):
    
    getiri.append((df[i]-df[i-1])/df[i-1])




