import random

print("****** Welcome to the PyPasswd Generator! ****** ".upper())

letters = int(input("How many letters would you like in your password ?: "))

symbols = int(input("How many symbols would you like? : "))

numbers = int(input("How many numbers would you like? : "))

letters_list = ["q", "w", "e", "r", "t", "y", "u", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "i", "z", "x",
                "c", "v", "b", "n", "m",
                "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X",
                "C", "V", "B", "N", "M", ]
symbols_list = [" ", "é", "!", "'", "#", "+", "$", "%" "&", "/", "{", "(", "[", ")", "]", "=", "}", "?", "/", "*", "-",
                ".", ",", "~", "´", ":", ";", ">", "<", "|", "_"]
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

password = []

for i in range(symbols):
    a = random.choice(symbols_list[0:-1])
    password.append(a)

for i in range(letters):
    a = random.choice(letters_list[0:-1])
    password.append(a)

for i in range(numbers):
    a = random.choice(numbers_list[0:-1])
    password.append(a)

random.shuffle(password)

converted_list = map(str, password)

password = ''.join(converted_list)

print("Password:", password)
