#girdiğin faktoriyeli hesaplama çalışması

sayi=int(input("Kaçıncı faktoriyeli hesaplayayım?:")) 

faktoriyel=1

if sayi<0:
    print("Negatif sayıların faktoriyeli hesaplanmaz")
elif sayi==0:
    print("Sonuc:1")
else:
    for i in range(1,sayi+1):  # artı 1,5 girdiysek 5 de dahil olsun diye artı 1 var.
        faktoriyel= faktoriyel * i
    print("Sonuc:",faktoriyel)
    