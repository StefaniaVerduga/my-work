# lab4.1.1isEven.py
# Author: Stefania Verduga
# This programs asks the user to enter in a number
# and the program will tell the user if the number is even or odd

number = int(input("Enter an integer: "))

if (number % 2) == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")