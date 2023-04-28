fruits = ["Apple","Peach","Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruits)

# For loop with Range
for number in range(1,11,3):
    print(number)

total = 0
for number in range(1,101):
    total += number
print(number)

total = 0
for number in range(2,101,2):
    total += number
print(total)

total2 = 0
for number in range(1,101):
    if number % 2 == 0:
        total2 += 2
print(total2)

# Don't 
student_heights = input("İnput a list of student heights ").split()

for n in range(0,len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
for height in student_heights:
    total_height += height
print(total_height)

number_of_students = 0
for student in student_heights:
    number_of_students +=1
print(number_of_students)

avarage_height = round(total_height / number_of_students)
print(avarage_height)

# Don't 2
student_score = input("Input a list of students Score").split()

for n in range(0,len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)

hight_score = 0
for score in student_score:
    if score > hight_score:
        hight_score = score
print(f"The highest score in the class is : {hight_score}")