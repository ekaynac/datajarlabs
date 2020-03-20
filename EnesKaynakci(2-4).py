# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 19:48:24 2020

@author: Enes
"""

x = input(''''Değeri giriniz:(xC ya da xF şeklinde)''')

if(x[-1] == "C"):
    value = x[:-1]
    value = int(value)
    value = (5/9) * (value - 32)
    print(value)

elif(x[-1] == "F"):
    value = x[:-1]
    value = int(value)
    value = (9/5) * value + 32
    print(value)
    
else:
    x = input('''Yanlış girdiniz bir daha deneyin(Örnek: 123F, 46C)''')
    


word = input("Tersine çevirilecek sözcüğü giriniz:")

word = list(word)


reverse_word = [word[x] for x in range(-1,-len(word)-1,-1)]



print(*reverse_word,sep=None)

    
    
fibonacci_set = [1,1]

while (fibonacci_set[-1] + fibonacci_set[-2] < 50):
    fibonacci_set.append(fibonacci_set[-1] + fibonacci_set[-2])
    
print(*fibonacci_set,end="\n")


multip = int(input("Çarpım tablosu oluşturulacak sayıyı giriniz:\n"))

for x in range(1,11):
    print("{} x {} = {}".format(multip,x,multip*x),end="\n")
    

the_list = [x**2 if x%2 == 1 else x**3 for x in range(1,21)]


print(*the_list)
