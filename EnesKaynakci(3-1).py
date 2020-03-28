# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 00:23:42 2020

@author: enes_
"""

import numpy as np
import pandas as pd

listt = pd.DataFrame()

rand_size= 512

mean = list()
mean_manual = list()
median = list()
varr = list()
varrddof = list()
std = list()
st_err = list()
values = np.arange(3*rand_size).reshape(3,rand_size)
counts = np.arange(3*rand_size).reshape(3,rand_size)


listt["First Random Set"]=np.random.rand(rand_size)
listt["Second Random Set"]=np.random.rand(rand_size)
listt["Third Random Set"]=np.random.rand(rand_size)

for i in listt:
    #Mean
    mean_manual.append(sum(listt[i])/len(listt[i]))
                         
    mean.append(np.mean(listt[i]))
    
    #Median
    median.append(np.median(listt[i]))
    
    #Variance
    varr.append(listt[i].var())
    varrddof.append(np.var(listt[i],ddof=1))
    ##Why are they same??
    
    #Standart Deviation
    std.append(np.std(listt[i],ddof=1))
    
for i in listt:
    for x in range(0,3):
         #Mode
        (values[x], counts[x]) = np.unique(listt[i], return_counts=True)
       
       #Standart Error
        st_err.append(std[x]/np.sqrt(rand_size))
        

    
   
        
    
                  