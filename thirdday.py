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