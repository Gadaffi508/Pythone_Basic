class MyClass:
    x=5
p1 = MyClass

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def _str_(self) :
        return f"{self.name} name of the ({self.age})"
    def myFunc(self):
        print("Hello my name is " + self.name)
p2 = Person("John",36)

p2.age = 37

print(p2.name)
p2.myFunc()

class Otomobil:
    def __init__(self,model,renk):
        self.renk = model
        self.model = renk
        self.hiz = 0

    def hareket_et(self):
        self.hiz = 1
        print("Haraket ediyor")

    def dur(self):
        self.hiz = 0
        print("araba durdu")

    def hizlan(self,yeni_hiz = 10):
        self.hiz += yeni_hiz
        print("Arabanın yeni hizi : " + self.hiz)

araba = Otomobil("Sari",2023)

sonuc = araba.hareket_et()
print(araba.hiz)
araba.dur()
print(araba.hiz)
araba.hizlan()
print(araba.hiz)

class Hesap:
    def __init__(self,_tür,_miktar):
        self.tür = _tür
        self.miktar = _miktar

    def para_çek(self,tutar):
        self.miktar -= tutar
        return f"Banka hesabınızdan {tutar} çekilmiştir."

    def para_yatır(self,tutar):
        self.miktar += tutar
        return f"Banka hesabınızdan {tutar} eklenmiştir."

    def __str__(self):
        return f"Banka hesabınıza {self.miktar} {self.tür} bulunmaktadır"
    
class Urun:
    def __init__(self,_adi,_fiyat):
        self.adi = _adi
        self.fiyat = _fiyat
class Sepet:
    ürünler = []
    def __init__(self,_ürün):
        self.ürünler.append(_ürün)

ayakkabı = Urun("Ayyakabı",500)
sepetimiz = Sepet(ayakkabı)