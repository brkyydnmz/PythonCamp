import sqlite3

def listele():
    baglanti = sqlite3.connect("chinook/chinook.db") #bu veri tabanına bağlanmaya yarar.
    cursor = baglanti.execute("select FirstName,LastName from customers")   #execute çalıştır demek

    for satir in cursor:
        print(satir[1])
    
    baglanti.close()

listele()  #sondaki defin ardında geleni yazıp parantez açmak fonksiyon çağırmadır.
