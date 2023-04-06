#faktoriyel
def faktoriyel(sayı):
    sonuc=1
    for i in range(2,sayı+1):
        sonuc = sonuc * i
    return sonuc
print(faktoriyel(5))
print("faktoriyel")

#faktoriyel
def f(sayı):
    if sayı==2:
        return 2
    return sayı *f(sayı-1)
print(f(5))
print("faktoriyel")

#1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
def fibonacci(n):
    if n<=2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
for i in range(1,12):
    print(fibonacci(i))# i yanına ,end=' ' ,end yan yana yazdırma
print("fibonacci bitti")

def us_al(sayı,us):
    if us==1:
        return sayı
    return sayı * us_al(sayı,us-1)
print(us_al(5,2))

dizi = [1,2,3,["a","b","c",[4,5],"d","e"],6,7,8,["f","g"]]
def duzlestır(seri):
    duz_zeri=[]
    for eleman in seri:
        if type(eleman) == list:
            duz_zeri.extend(duzlestır(eleman))
        else:
            duz_zeri.append(eleman)
    return duz_zeri
print(duzlestır(dizi)) #bir diziyi alt elamanları dahil tek bir liste dönüştür
print("dizi düzleştirme bitti")

mesela = "ey edip adanada pide ye"
kayak = "kayak"
olumsuz = "olumsuz"
def palindrom(kelime):
    if len(kelime)<2:
        return True
    if kelime[0]==kelime[-1]:
        return palindrom(kelime[1:-1])
    else:
        return False
print(palindrom("alimmlia"))
print("palin bitti")

bulmaca = [[0,0,1,6,0,0,5,8,0],
[2,0,1,6,0,0,5,1,0],
[8,0,0,6,0,0,5,2,0],
[5,0,0,6,0,0,5,4,0],
[0,1,0,6,0,0,5,7,0],
[0,8,0,6,0,0,5,8,6],
[0,2,0,6,0,5,0,8,9],
[0,9,0,6,4,7,0,0,8],
[0,7,5,6,0,9,4,0,0]]

def boshücrebul(grid):
    for satır in range(9):
        for sütun in range(9):
            if grid[satır][sütun] ==0:
                return satır,sütun
    return None

def kontrol(grid,satır,sütun,sayı):
    for i in range(9):
        if grid[satır][i]==sayı:
            return False
    for i in range(9):
        if grid[i][sütun]==sayı:
            return False
    kk_satır = (satır//3) * 3
    kk_sütun = (satır//3) * 3

    for i in range(3):
        for j in range(3):
            if grid[kk_satır+i][kk_sütun+j]==sayı:
                return False

    return True

def sudoku(grid):
    bosluk = boshücrebul(grid)

    if not bosluk:
        print("sudoku çözüldü")
    
    satır,sütun=bosluk 
    for i in range(1,10):
        if kontrol(grid,satır,sütun,i):
            grid[satır][sütun] = i

            if sudoku(grid):
                return True
            grid[satır][sütun] = 0
    return False
print(sudoku(bulmaca))
print(bulmaca)