hafta_gunleri = {"1":"Pazartesi",
                 "2":"Salı",
                 "3":"Çarşamba",
                 "4":"Perşembe",
                 "5":"Cuma",
                 "6":"Cumartesi",
                 "7":"Pazar",
    }

print(*list(hafta_gunleri.values()),sep="\n")


chosen1 = input("Silmek istediğiniz günün numarasını girin:")
chosen2 = input("Silmek istediğiniz günün numarasını girin:")


del hafta_gunleri[chosen1]
del hafta_gunleri[chosen2]
print("\n","Kalan günler:\n ")
print(*list(hafta_gunleri.values()),sep="\n",end="\n")

raw_list =["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran",
           "Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık",
           31,28,31,30,31,30,31,31,30,31,30,31]

month_list = raw_list[:12]
daycount_list = raw_list[12:]

seperated_list = [month_list,daycount_list]

winter = raw_list[0:-22]
winter.append(raw_list[-13])
spring = raw_list[2:5]
summer = raw_list[5:8]
autumn = raw_list[8:11]

summer_duration = 0

for x in summer:
    
    i = seperated_list[0].index(x)
    
    summer_duration = summer_duration + seperated_list[1][i]
    
print("\n","Yaz ayının süresi:\n",summer_duration)