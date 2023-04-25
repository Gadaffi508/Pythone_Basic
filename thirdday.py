print("Welcome to the rollercoaster!")
heigth = int(input("What is your heigth in cm ? "))
bill = 0
if heigth >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age ? "))
    if age < 12:
        print("Child tickets are $5.")
        bill = 5
    elif age < 18:
        print("You tickets are $7.")
        bill = 7
    elif age >= 45 and age <55:
        print("Everything is going to be ok. Have a free ride on us!")
    else :
        print("Adult tickets are $12.")
        bill = 12

    wants_photo = input("Do you want a photo taken ? Y or N. ")
    if wants_photo == "Y":
        print()
        bill += 3
    print(f"Your final bill is {bill}")
else:
    print("Sorry, you have to grow taller before you can ride")

# Don't change the code below
number = int(input("Which number do you want to change "))
# Don't change the code above

# write your code below this line
if number % 2 == 0 :
    print("this is a even number.")
else:
    print("this is an add number")

# Don't change the code below
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in m: "))
# Don't change the code above

#write your code below this line
bmi = round(weight / heigth ** 2)
if bmi < 18.5:
    print(f"your bmi is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"your bmi is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"your bmi is {bmi}, you are overweight.")
elif bmi < 35:
    print(f"your bmi is {bmi}, you are obese.")
else :
    print(f"your bmi is {bmi}, you are clinically obese.")


# Don't change the code below
year = int(input("Which year do you want to check ? "))
# Don't change the code above

# write your code below this line
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else :
        print("leap year.")
else:
    print("Not leap year")

# Don't change the code below
print("Welcome to Pythone Pizza Deliveries!")
size = input("What size pizza do you want ? S, M or L ")
add_pepperon = input("Do you want pepperon ? Y or N ")
extra_chesse = input("Do you want extra chesse ? Y or N")
# Don't change the code above

# write your code below this line
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill +=25

if add_pepperon == "Y":
    if size == "S":
        bill +=2 
    else:
        bill +=3
if extra_chesse == "Y":
    bill +=1
print(f"Your final bill is ${bill}")

# Don't change the code below
print("Welcome to the love Calculator!")
name1 = input("What is your name ? \n")
name2 = input("What is their name ? \n")
# Don't change the code above

# Write your code below this line
combined_string = name1 + name2
lower_case_string = combined_string.lower()
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

truee= t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(truee) + str(love))
if love_score < 10 or love_score > 90 :
    print(f"Your love score is {love_score}, you go together like coke and mentos")
elif love_score >= 40 and love_score <= 50 :
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")


print("Welcome to Tresure  Island.")
print("Your mission is to find treasure.")
choice1 = input('You\'re at a crossroad, where do you want to go ? Type "left" or "right".\n').lower()
if choice1 == "left":
    choice2 = input('You\'ve come to a lake. there is an island in the middle of the lake. Type "wait" to wait for a boat.Type "swim" to  swim across').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and onw blue. Which colour do you choose ? ")
        if choice3 == "red":
            print("It's a room full o fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over")
        else :
            print("You chose a door that doesn't exist. Game Over")
    else:
        print("You got attacked by an angry trout. Game Over")
else :
    print("You fell into a hole. Game Over")