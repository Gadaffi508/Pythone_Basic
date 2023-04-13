import random
random.random() # random sayı üretme
print(random.random())
random.seed(10) #sayı 10 dan baz alıyor
print(random.random())
random.randint(1,10) # 1 ile 10 arasnda ramdon sayı üretir
print(random.randint(1,10))
#a = input()
#print(a)
print("Sayı giriniz : ")
sayı =5#sayı = int(input("Tam sayı olsun")) 
for i in range(sayı):
    print(i)
def asal(number):
    for i in range(2,number):
        if number%i==0:
            return False
        return True
print("Sayı giriniz :")
#num = int(input("Sayı giriniz : "))
num =5
if asal(num):
    print(num," Sayısı asaldır")
else:
    print(num," Sayısı asal değildir")

def Sifrele(metin):
    sifrele = ""
    alfabe = "qwertyuıopğüasdfghjklşizxcvbnmöçQWERTYUIIOPĞÜASDFGHJKLŞİZXCVBNMÖÇ.:;?*/"

    for harf in metin:
        x=alfabe.find(harf)
        random.seed(x)
        sayı = random.randint(0,len(alfabe))
        sifrele += alfabe[sayı]

    return sifrele
print(Sifrele("Yusuf"))

def SifreCoz(metin):
    cozüm = ""
    alfabe = "qwertyuıopğüasdfghjklşizxcvbnmöçQWERTYUIIOPĞÜASDFGHJKLŞİZXCVBNMÖÇ.:;?*/"

    for harf in metin:
        for x in range(len(alfabe)):
            random.seed(x)
            sayı = random.randint(0,len(alfabe)-1)
            if harf == alfabe[sayı]:
                cozüm += alfabe[x]

    return cozüm
print(SifreCoz("üğWğv"))


