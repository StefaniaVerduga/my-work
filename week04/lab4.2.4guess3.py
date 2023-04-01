# lab4.2.4guess3.py
# The program prompts the user to guess a random number previously generated,
# the program will tell the user if there guess is too high or too low.
# Author: Stefania Verduga

import random

number = random.randrange(0,100)
guess = int(input("Please, guess the number: "))
while guess != number:
    if guess < number:
        print("too low")
    else:
        print("too high")
    guess = int(input("Please, guess again: "))

print("Well done! Yes, the number was ",number)
