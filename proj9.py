#its a password generator
import random

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!#$%&()*+'

def password_generator(number_of_letters, number_of_symbols, number_of_numbers):
    password = ""
    for i in range(number_of_letters):
        password += random.choice(letters)
    for j in range(number_of_symbols):
        password += random.choice(symbols)
    for k in range(number_of_numbers):
        password += random.choice(numbers)
    print(password)

password_generator(4, 2, 2)