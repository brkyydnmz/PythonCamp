#köşeli parantez görülen yapılara [] list denir.
#.append list e ekleme yapar.Başına kaydedilecek list i seçiyoruz.


urunler=["Laptop","Mouse","Keybord"]
print(urunler)
print(type(urunler))

urunler.append("Telefon")
print(urunler)

ogrenciler1=["Engin","Cavit","Berkay"]
ogrenciler2=["Kerem","Halil","Murat"]
ogrenciler1=ogrenciler2    #bu ogrenciler1 inkileri bırak ogrenciler2 ninkileri tut diyor
ogrenciler2[0]="Engin"    #0 dan saymaya başlanır o yüzden 0 dedik ilk indeks 0dır.Kerem bu ile Engin oldu.
print(ogrenciler1)    
print(ogrenciler2)


sayi1=10
sayi2=20
sayi1=sayi2    #sayi1 sonucu sayi2 sonucu yerine geçti değer tip olduğu için.
sayi2=60        #sayi2 60 oldu burda
print(sayi2)  
print(sayi1)  

#referans tip--> list(diziler yani)
#değer tip--> interface,float,boolean

isim="Engin"
print(isim[0],isim[1])

bosListe=[]