def faktoriyel(sayi):
    sonuc=1
    for i in range(2,sayi+1):
        sonuc *= i
    return sonuc
print(faktoriyel(5))    

def topla(a,b):
    return a+b
print(topla(2,5))
mesaj1 = "Dünya"
def mesajver():
    global mesaj2 # global diyerek mesa2 nin başka bir yerde çağrılmasını sağladık
    mesaj2 = "Merhaba"
mesajver()
print(mesaj1)
print(mesaj2)
f = lambda x,y : x+y
print(f(5,7))
mylist = [1,2,4,5,6,9,77]
filtrliste = list(filter(lambda x: x>5,mylist))
print(filtrliste)
dizi = [-i if i%2==1 else i for i in range(1,6)]
print(dizi)