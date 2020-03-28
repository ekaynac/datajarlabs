# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 10:01:02 2020

@author: enes_
"""


import matplotlib.pyplot as plt
import pandas as pd


sales = pd.read_csv("vgsales.csv",index_col = "Rank")

sales = sales[['Platform', 'Year']]




plt.figure()

## XBOX 360
plt.subplot(1,2,1)

sales_xbox = sales.loc[lambda df: sales['Platform'] == "X360", :]

sales_xbox["count"] =1
                              
x_xbox = sales_xbox.groupby(by = "Year").sum()

plt.bar(x= x_xbox.index ,height = x_xbox["count"], color="purple")

plt.xlabel('Yıl')

plt.title('Xbox 360 Satışları')


## PS3
plt.subplot(1,2,2)

sales_ps3 = sales.loc[lambda df: sales['Platform'] == "PS3", :]

sales_ps3["count"] =1
                              
x_ps3 = sales_ps3.groupby(by = "Year").sum()

plt.bar(x= x_ps3.index ,height = x_ps3["count"],color="green")

plt.xlabel('Yıl')

plt.title('PS3 Satışları')
 


