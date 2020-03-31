# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 17:06:44 2020

@author: enes_
"""


import pandas as pd


## PART 1
df = pd.read_csv("states_all.csv")

df.info()


missing_percent = df.isnull().sum()*100/df.shape[0]
dfilled= df

## PART 2
# Yüzdelik olarak çok eksik olan sütunları doldurmak anlamsızdır.
# Çok uç değerlerde olan
for x in df.iloc[0:1918,3:21]:
    dfilled[x] = df[x].fillna(df[x].mean())
    
missing_percent2 = df.isnull().sum()*100/df.shape[0]



## PART 3


mean_yearly= df.groupby(by="YEAR").mean()

  

##PART 4  



