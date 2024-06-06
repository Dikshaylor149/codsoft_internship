import random

import string

length = int (input("Enter the length:"))

print(string.ascii_letters)

print(string.digits)

print(string.punctuation)

chars = string.ascii_letters
chars+= string.digits
chars+= string.punctuation

password=''.join( [random.choice(chars) for i in range(length)])

print("your random password is:", password)
