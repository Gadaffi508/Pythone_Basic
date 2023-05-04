import random
import Hesap as h # ismi kısaltma
import sqlite3 as sql


sonuc = h.Topla(5,9)

print(sonuc)


veritabanı = sql.connect("deneme.sqlite")
imlec = veritabanı.cursor()

imlec.execute("CREATE TABLE tablo (isim, soyisim)")
imlec.execute('INSERT INTO tablo (isim, soyisim) values ("Yusuf","Arslan")')

def Listele():
    imlec.execute("Select * from tablo")
    veriler = imlec.fetchall()
    for veri in veriler:
        print(veriler)
print(Listele())

veritabanı.commit()

veritabanı.close()