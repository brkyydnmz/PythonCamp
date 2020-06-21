istenenKredi = 100000
hesap=9555
minimumOlmasiGerekenHesap=10000
# (:) işareti bloğunu açacağım demek 
# if çalışmazsa else devreye girer çalışır yani burda paramız yetersizse else devreye girer.
#elif bütçesi 10 binden az ama kredi almak istiyor 9 bine eşit yada fazla durumda müdüre sorulacak
#and ve görevi görür 2 durumu kuralı da doğru olmalı, 2 kuraldan biri doğru olsun dersen or çalışır.


if hesap>=minimumOlmasiGerekenHesap:
    print("kredi verilebilir")
    print("ödemeler hesaplandı")    
elif hesap>=9000 and hesap<=9500:
    print("Müdüre sorulacak")
elif hesap>=9501 and hesap<=9999:
    print("Genel müdüre sorulacak")
else:
    print("Kredi almak için bakiyeniz yetersiz")


print("işlem sonu")
