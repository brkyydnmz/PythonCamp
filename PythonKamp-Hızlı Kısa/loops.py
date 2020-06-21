sehirler=["Ankara","İstanbul","İzmir"]

for sehir in sehirler:  #for sehir yazarsan sehirler listesinin içindeki elemanlar yazılır.
     print(sehir)


#range(5)=0 dan 5 e kadar tam sayıları verir.
#range(1,5)=1 den başlayıp 5 e kadar tam sayıları verir.
#range(5,24,3)=5 ten başlayıp 3 er artarak 24 ten küçük tam sayıları verir.

for sayi in range(1,10,2):   #1 başlangıç sayısı 10 a kadar 2 daha artar tek sayılar.     
     print(sayi)
sayac=1


#while if gibi koşul içerir.
#while döngüsünde kendimiz arttırma işlemi yapmalıyız yoksa döngüye girer.
while sayac<=10:   
    print(sayac)
    sayac= sayac + 1  #sayac++ da aynı şeydir.


isim=input("Adınız") #input ile kullanıcıdan bilgi alınır.
print("isim: "+isim)

 