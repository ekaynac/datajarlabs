# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 14:48:38 2020

@author: enes_
"""


import pandas as pd
import numpy as np
import math



#part1
def asalmi(x):
    flag=0
    for i in range(2,int(math.sqrt(x))):
        if(x%i == 0):
            flag +=1
        else:
            continue
    if flag ==0:
        return True
    else:
        return False

def fibolen(x):
    fib= [1,1]
    i=1
    while(i<x-1):
        fib.append(fib[-1]+fib[-2])
        i+=1
    return fib
        




indeks = ["a","b","c","d","e","f","g","h","i","j"]

my_dataframe = pd.DataFrame(index =indeks)

arr_asal = list()
i=2
while(len(arr_asal)<10):
    if (asalmi(i)):
        arr_asal.append(i)
    i+=1

my_dataframe["Asal Set"] = arr_asal

my_dataframe["Fibonacci Set"] = fibolen(10)




#part2
train_set = pd.read_csv("train.csv",index_col =0)                        

agemeanpersex = train_set.groupby(by="Sex").mean()["Age"]
                                                       
print(agemeanpersex,"\n")

sett = train_set[train_set["Age"] > 30]

i = len(sett[sett["Survived"]==0]                   )
j = len(sett[sett["Survived"]==1])

survivalratio = j/(i+j)

print("30 yaş altı ölüm oranı: {}\n".format(survivalratio))

sett = train_set[train_set["Sex"] == "male"]

i = len(sett[sett["Survived"]==0])
j = len(sett[sett["Survived"]==1])

survivalratioforman = j/(i+j)
print("Erkeklerde 30 yaş altı ölüm oranı: {}\n".format(survivalratioforman))

sett = train_set[train_set["Sex"] == "female"]

i = len(sett[sett["Survived"]==0])
j = len(sett[sett["Survived"]==1])

survivalratioforwoman = j/(i+j)
print("Kadınlarda 30 yaş altı ölüm oranı: {}".format(survivalratioforwoman))
    
    

    

















