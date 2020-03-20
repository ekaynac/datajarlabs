# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:55:56 2020

@author: enes_
"""


with open("yasamayadair.txt", "r", encoding='utf8') as f:
    lines = f.readlines()
    
    
    
print("Şiirin dize sayısı = {}".format(len(lines)))

first_word = []

for x in lines:
    x=list(x)
    for i in len(x):
        if (i != ' '):
            first_word[x].append(i)
        else:
            break
            