# Suggests a password based on the input requirements
import random
# Lists of all the components a password can have
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = []
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
for x in range(0,10):
    numbers.append(str(x))
print(len(alphabet))
print(len(numbers))
print(len(symbols))

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
password = ''
for letter in range(0, nr_letters):
    password += alphabet[random.randint(0, 51)]
for symbol in range(0, nr_symbols):
    password += symbols[random.randint(0, 8)]
for number in range(0, nr_numbers):
    password += numbers[random.randint(0, 9)]

# Randomizes the sequence of selected password components
random_password = ''.join(random.sample(password, len(password)))

print(f"Your suggested password is {random_password}")