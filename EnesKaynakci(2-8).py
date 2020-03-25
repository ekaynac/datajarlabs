# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 10:01:02 2020

@author: enes_
"""


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


sales = pd.read_csv("vgsales.csv",index_col = "Rank")

sales = sales[['Platform', 'Year']]

sales = sales.loc[lambda df: sales['Platform'] == "X360", :]

sales["count"] =1
                              
x = sales.groupby(by = "Year").sum()

plt.bar(x,height=x.count , align='center', alpha=0.5)


