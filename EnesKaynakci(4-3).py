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

## PART 2

# Yıl değişkenini atarsak verileri statelerine göre gruplarım
#ve statelerin eksik değerlerini o statein ortalamalarıyla doldururum

## PART 3

y=df.groupby("YEAR").mean()

y=df.groupby("YEAR").fillna(df.groupby(by="YEAR")).mean()
