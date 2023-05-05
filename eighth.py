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

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','y','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','y','w','x','y','z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt : \n")

text = input("Type your message: \n ").lower()
shift = int(input("Type the shift number : \n"))

def ceaser(start_text, shift_amount, cipher_direction):
    end_text = ""
    for letter in start_text:
        position = alphabet.index(letter)
        if cipher_direction == "decode":
            shift_amount *= -1
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"The {cipher_direction} text is {end_text}")

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        poisition = alphabet.index(letter)
        new_position = poisition + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text,shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"The decoded text is {plain_text}")

ceaser(start_text=text,shift_amount=shift,cipher_direction=direction)