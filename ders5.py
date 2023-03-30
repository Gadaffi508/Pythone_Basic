kare =  lambda x:x**2 
#print(kare(5))# çıktısı 25 
liste = [2,3,4,5,6,7,8,9,10]
def kontrol(sayı):
    if sayı>5:
        return True #beşten büyükse true döndür
    return False# değilse false
buyukler =list(filter(kontrol,liste))#5 ten büyük sayı yazdırma
kontrol2 = lambda sayı:True if sayı>5 else False #sayı 5 ten büyükse true değilse false
buyukler3=list(filter(lambda sayı:True if sayı>5 else False,liste)) # kısaca fonksiyon
liste2= [1,2,3,4,5,6,7,8,9,10]
def ekle(n) :
    return n+1
ekli_liste=list(map(ekle,liste2)) # birer fazla yazdır
liste3=[1,2,3,4,5,6,7,8,9,10]
from functools import reduce
toplamlar = reduce(lambda x,y:x+y,liste3)
liste4=[1,2,3,4,5,6,7,8,9,10]
def topla(a,b):
    return a+b
toplamlar2=reduce(topla,liste4)
metin = "Merhaba beni ters çevir"
parçalı = metin.split()
parçalı.reverse()
bütün= "i".join(parçalı)
def ters(ifade):
    parçalı=ifade.split()
    parçalı.reverse()
    return " ".join(parçalı) #girdiğimiz metnin kelimelerini ters çevirip veriyor
def bolemmi(a,b):
    if a%b==0:
        return True
    False
print(bolemmi(10,5))
