# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 13:46:05 2020

@author: enes_
"""


capital_init=1000

capital = 1000

for x in range(1,8):
    capital = capital +12/100*capital
    
print('''Hafta başında {} dolarlık bitcoin aldığımızda günde ortalama %12 
      kazançla, bir hafta sonunda {:.2f} dolar kazanırdık'''.format(capital_init,capital))


inpp = input("Dosya ismini giriniz: ")
print("{}.py".format(x))