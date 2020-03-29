# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 14:34:58 2020

@author: enes_
"""

import numpy as np
import pandas as pd

meanvar2 = pd.DataFrame()
meanvar1 = pd.DataFrame()


varr2=pd.DataFrame()
varr1=pd.DataFrame()

for i in range(0,50):
    varr2[i]=np.random.normal(-1, 1, 1000)
    meanvar2[i]=varr2.mean()
    
for i in range(0,1000):
    varr1[i]=(np.random.normal(1, 2, 1000))
    meanvar1[i]= varr1.mean()
    
    
    
    