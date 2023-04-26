import random

random_integer = random.randint(1,10)
print(random_integer)

random_float = random.random()
print(random_float)

love_score = random.randint(1,100)
print(f"Your love score is {love_score}")

random_side = random.randint(0,1)
if random_side == 1:
    print("Heads")
else :
    print("Tails")

states_of_Turkısh = ["Nevşehir","Niğde","Ordu","Osmaniye","Rize","Sakarya","Samsun","Şanlıurfa","Siirt","Sinop","Sivas","Şırnak","Tekirdağ","Tokat"]

states_of_Turkısh.append("Bursa")

states_of_Turkısh.extend("Ordu","Oltu")

# split string method
names_string = input("Give me everbody's names, seperated by a comma.")
names = names_string.split(", ")
num_items = len(names)
random_choice = random.randint(0,num_items-1)
person_who_will_pay = names[random_choice]
person_who_will_pay_demo = random.choice(names)
print(random_choice)

dirty_dozen = ["Strawberries","Spinach","Kale","Nectarines","Apples"]

fruits = ["Strawberries","Nectarines","Apples","Grapes","Peaches"]

vegetables = ["Spinach","Kale","Tomatoes","Celery","Potatoes"]

dirty_dozen = [fruits,vegetables]

row1 = ["😁","😆","😅"]
row2 = ["😍","🥰","😘"]
row3 = ["😎","🥸","🤩"]
map = [row1,row2,row3]
print(f"{row1} \n {row2} \n {row3}")
position = input("Where do you want to put the treasure ? ")

horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical-1]
selected_row[horizontal-1] = "X"