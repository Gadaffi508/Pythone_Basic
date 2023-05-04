# greet() adında bir fonksiyon yarat
# Fonksiyonun içine 3 print deyimi yaz
# greet() işlevini çağırın ve kodunuzu çalıştırın.
import math
import random

def greet():
    print("3 print deyimi")
    print("2 print deyimi")
    print("1 print deyimi")
print(greet())

def greet_with_name(name):
    print(f"Hello {name}")
print(greet_with_name(input("What is your name ? ")))

def greet_withs(height,weight):
    print(f"Your height {height} and Your weight {weight}")
height = input("What is height ? ")
weight = input("What is weight ? ")
print(greet_withs(height,weight))

def paint_calc(height,width,cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"You'll need {num_of_cans} cans of paint")

def prime_checker(number):
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
        if is_prime :
            print("İt's a prime number")
        else :
            print("İt's not a prime number")

n = int(input("Check this number : "))
prime_checker(number = n)