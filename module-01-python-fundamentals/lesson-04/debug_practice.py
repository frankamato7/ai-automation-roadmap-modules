import os

#Debug no.1
def add_numbers(a, b):
    result = a + b
    return result

#Debug no.2
try:
    num = int(input("Enter a number: "))
    print(num * 2)
except ValueError:
    print('Not a valid number!')

#Debug no.3
try:
    with open("data.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print('File not found!')