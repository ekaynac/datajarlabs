# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 14:34:59 2020

@author: enes_
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



dagilim = np.random.normal(0.1,0.1,1000)

df = pd.DataFrame()

df =pd.read_csv("GOOG.csv")

df = df["Open"]

plt.figure()

plt.hist(df, bins = 50 )

plt.hist(dagilim, bins = 50 )