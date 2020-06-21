#class oluşturma amacı mantıksal bir araya getirmek içindir.
#self sınıf içerisinde metotlara,parametrelere ulaşmak için kullanılanilir.

class Banka:
    def krediBasvur(self):
        print("Kredi başvurusu yapıldı") 

    def krediHesapla(self):
        print("Hesaplar yapıldı")

banka=Banka()
banka.krediBasvur()

#self = this