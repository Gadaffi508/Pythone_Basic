sıcaklık = int(input("Sıcaklık giriniz :"))
if(18<sıcaklık and sıcaklık<30) : print("true")
else : print("false")

Hız=int(input("hız giriniz :"))
dgm = input("Doğum gününüz mü ?")
if(dgm == "evet") : Hız-5
if(Hız<65) : print("cezanız yok")
elif(Hız>65 and Hız<80) : print("cezanız var")
else : print("cezanız yüksek")


