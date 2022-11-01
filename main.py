'''
Generator: This code helps to generate a strong password
'''
import random
SPECIAL_CHARACTERS = ['&', '#', '$', '!', '?', '"', '(', ')', '.']

ALPHABETIC_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'
                         'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                         'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                         'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
password_list = []
password = ""

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

for i in range(1, nr_letters + 1):
    password_list += random.choice(ALPHABETIC_CHARACTERS)
for i in range(1, nr_symbols + 1):
    password_list += random.choice(SPECIAL_CHARACTERS)
for i in range(1, nr_numbers + 1):
    password_list += random.choice(NUMBERS)
random.shuffle(password_list)
for i in password_list:
    password += i
print(f"Your password is {password}")
