#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# letters_length = len(letters)
# numbers_length = len(numbers)
# symbols_length = len(symbols)

# password = ""
# for i in range(nr_letters):
# 	int_generated = random.randint(0, letters_length)
# 	password += letters[int_generated]

# for i in range(nr_symbols):
# 	int_generated = random.randint(0, symbols_length)
# 	password += symbols[int_generated]

# for i in range(nr_numbers):
# 	int_generated = random.randint(0, numbers_length)
# 	password += numbers[int_generated]

# print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
letters_length = len(letters)
numbers_length = len(numbers)
symbols_length = len(symbols)

chars = []

password = ""
for i in range(nr_letters):
    int_generated = random.randint(0, letters_length - 1)
    chars.append(letters[int_generated])

for i in range(nr_symbols):
    int_generated = random.randint(0, symbols_length - 1)
    chars.append(symbols[int_generated])

for i in range(nr_numbers):
    int_generated = random.randint(0, numbers_length - 1)
    chars.append(numbers[int_generated])

password = ""
while len(chars) > 0:
    char_pop = random.randint(0, len(chars) - 1)
    password += chars.pop(char_pop)

print(password)