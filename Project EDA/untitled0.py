# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 10:01:02 2020

@author: enes_
"""


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("full_data.csv")


df_nnzero = df[df.total_cases != 0]

x = 0
y = 0
threshold = 30
for i in range(len(df_nnzero.groupby(by="location"))):
    if (df_nnzero.groupby(by="location").count() > threshold)["date"][i] == True:
        x += 1
print(" {} country have more than {} day data".format(x,threshold))


for i in range(len(df_nnzero.groupby(by="location"))):
    if (df_nnzero.groupby(by="location").count() > threshold)["date"][i] == False:
        y += 1
print(" {} country have less than {} day data".format(y,threshold))

df_nnzero.groupby(by="location").count() > threshold

df_nnzero.reset_index(inplace= True)

th_country_list = list()
for i in range(len(df_nnzero.groupby(by="location"))):
    if ((df_nnzero.groupby(by="location").count()).date[i] > threshold) == True:
        th_country_list.append((df_nnzero.groupby(by="location").count()).index[i])
        
df_thresh = pd.DataFrame()

for count in range(len(df_nnzero)):
    for countryname in th_country_list:
        if (df_nnzero[df_nnzero.index == count]["location"] == countryname).bool():
            df_thresh.append(df_nnzero[df_nnzero.index == count])
            
    