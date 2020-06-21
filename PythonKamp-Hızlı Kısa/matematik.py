class Matematik: #self demek class ın kendisi
    def __init__(self,sayi1,sayi2):  #constructor(yapıcı) blok init
        self.s1=sayi1
        self.s2=sayi2
        print("Matematik başladı(referansı oluştu)")
    def topla(self):
        return  self.s1 + self.s2   #buradaki self Matematiğin sayi1 sayi2 sine dönüştürmeye yaradı
    def cikar(self):
        return self.s1 - self.s2
    def bol(self):
        return self.s1 / self.s2
    def carp(self):
        return self.s1 * self.s2

#Matematik yanındaki 6 ve 7 def__init__ teki sayi1 ve sayi 2 ye tekamül eder.
matematik = Matematik(6,7)  #buradaki Matematik initle alakalıdır.içine yazılan sayı inittendir.
sonuc = matematik.carp()   #topla yazan yere topla cikar bol yazıp uygulayabilirsin.
print("Sonuç : " + str(sonuc)) 

#super demek onun baz aldığı sınıfın kendisidir.
#Istatistik te direk matematiği kullanmak istediğimiz için direk matematiği inheritance(__init__) ettik.
#Matematikten miras alıyoruz Istatistik için miraz __init__ ile olur.

class Istatistik(Matematik):
    def __init__(self, sayi1, sayi2):
        super().__init__(sayi1,sayi2)  #super miras ile çalışmada kullanılır miras alırken.
    def varyansHesapla(self):
        return self.s1 * self.s2

istatistik = Istatistik(5,8)
