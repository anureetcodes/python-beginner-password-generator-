# This program generates a random password using:
# - Letters
# - Numbers
# # - Symbols
# The user can choose how many of each character to include.

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the Python Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password_list=[]
for character in range(0,nr_letters):
    password_list.append(random.choice(letters))

for character in range(nr_symbols):
    password_list.append(random.choice(symbols))

for character in range(0,nr_numbers):
    password_list.append(random.choice(numbers))
print(password_list)
random.shuffle(password_list)
print(password_list)
password= ""
for char in password_list:
    password += char

print( f"Your password is: {password}")
#checking password strength
length = len(password)
if length < 6:
    print(" Your Password Strength is: Weak")
elif length <= 10:
    print(" Your Password Strength ia: Medium")
else:
    print("Your Password Strength is: Strong")