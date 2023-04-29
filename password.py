import random

letters = ['a','b','c','d','e','f','g','ğ','h','ı','i','k','l','m','n','o','ö','p',
           'A','B','C','D','E','F','G','Ğ','H','I','İ','K','L','M','N','O','Ö','P',
           'r','s','ş','t','u','ü','v','y','z','R','S','Ş','T','U','Ü','V','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input(f"How many letters would you like in your password ? \n"))
nr_symbols = int(input(f"How many symbols would you like ? \n"))
nr_numbers = int(input(f"How many numbers would you like ? \n"))

# Easy
password = ""

for char in range(1,nr_letters + 1):
    password += random.choice(letters)

for char in range(1,nr_symbols + 1):
    password += random.choice(symbols)
    
for char in range(1,nr_numbers + 1):
    password += random.choice(numbers)

print(password)

# Hard
password_list = []

for char in range(1,nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1,nr_symbols + 1):
    password_list.append(random.choice(symbols))
    
for char in range(1,nr_numbers + 1):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char
print(f"Your password is : {password}")