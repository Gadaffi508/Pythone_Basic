def my_function():
    for i in range(1,21):
        if i == 20:
            print("You got it")
my_function()

import random

dice_imgs = ["1","2","3","4","5","6"]

dice_num = random.randint(0,5)

print(dice_imgs[dice_num])

year = int(input("What's your year of birth ? \n"))
if year > 1980 and year < 1994:
    print("You're a millenail.")
elif year >= 1994:
    print("You are a Gen Z")

age = int(input("How old are you ? \n"))
if age > 18:
    print(f"You can drive at age {age}")

pages = 0
word_per_page = 0
pages = int(input("Number of pages : \n"))
word_per_page = int(input("Number of words per page : \n"))
total_words = pages * word_per_page
print(f"pages = {pages}")
print(f"word_per_pages = {word_per_page}")
print(total_words)

def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)

mutate([1,3,5,7,9,11,13,15])

number = int(input("Which number do you want to check ? \n"))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an add number")

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year ")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number) 