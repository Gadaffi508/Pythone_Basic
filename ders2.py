for i in range(20,0,-2):
    if i == 4:
        break
    if i == 12:
        continue
    print("Sıradaki sayımız: " + str(i))
else :
    print("bitii")
liste = [1,2,3,4,5,6,7,8,9,10]
kontrol = [2,4,6,8]
buyukler = []
for i in liste:
    if kontrol(i):
        buyukler.append(i)
print(buyukler)
liste = [1,2,3,4,5,6,7,8,9,10]
ekli_liste = list(map(lambda n : n+1,liste))
eksi = lambda n : -n if n%2==1 else n
ekli_liste = list(map(lambda n: n if n%2==0 else -n,liste))
print(ekli_liste)
#Oparatörler
x=15
y=4
print('x + y = ', x+y)
print('x - y = ', x-y)
print('x * y = ', x*y)
print('x / y = ', x/y)
print('x % y = ', x%y)
print('x // y = ', x//y)
print('x ** y = ', x**y)