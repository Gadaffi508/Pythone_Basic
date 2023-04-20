#String

print("Hello"[0])
print("123"+"567")

#Integer

print(123 + 567)

#float

print(3.1 + 4.5)

#Boolean

True or False

num_char = len(input("What is your name ? "))
print("Your name has ",num_char," charecters.")
print(type(num_char))

num_char = len(input("What is your name ? "))
new_num_char = str(num_char)
print("Your name has "+new_num_char+" charecters.")

#Mathematical
3 + 5
7 - 4
3*2
6/3
2 ** 2 #üssü = 4 2**3 =8

#PEMDASLR
#()
#**
#*/
#+-

print(3*3+3/3-3)

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

bmi=int(weight)/float(height) ** 2
bmi_as_int=int(bmi)
print(bmi_as_int)

print(round(8/3)) #8/3 = 2.666 round =3
print(8//3) #2.67

score =0
height = 1.8
isWinning = True
#f-String
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

#year
age = input("What is your current age ? ")
age_as_int = int(age)

year_remaining=90-age_as_int
days_remaining=year_remaining*365
weeks_remaining=year_remaining*52
months_remaining=year_remaining*12

message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left"
print(message)

#Round the result to 2 decimal places = 33.60
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill ? $"))
tip = input("How much tip would you like to give? 10, 12 or 15 ? ")
people = int(input("How many people to split the bill?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person,2)
#final_amount = "{:.2f}".format{bill_per_person}
print(f"Each person should pay : ${final_amount}")