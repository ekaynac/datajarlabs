# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:55:56 2020

@author: enes_
"""


## part 1
with open("yasamayadair.txt", "r", encoding='utf8') as f:
    lines = f.readlines()
    
    
    
print("Şiirin dize sayısı = {}\n".format(len(lines)))




for x in lines:
    print(x[:x.index(" ")])






##part2
number = input("Asallığı kontrol edilecek sayıyı giriniz:")
number = float(number)

flag=0
for n in range(2,int(number**(1/2))+1):  
    if(number%n == 0):
        flag = flag + 1
    else:
        continue

if(flag!=0):
    print("Girdiğiniz sayı asal değil".format(number))
else:
    print("Girdiğiniz sayı  asal")
    
    



##part3
inpp = list(input("Listelenecekleri giriniz:"))
inpp.sort()
temp= 0
i=int(0)
while(i<len(inpp)):
    if(temp == inpp[i]):
        del inpp[i]
    else:
        temp = inpp[i]
        i += 1
        
        
##part4
from datetime import date
def calculate_age(born_date):
    today = date.today()
    age = today.year - born_date
    return age

calculate_age()
    
        



    
        