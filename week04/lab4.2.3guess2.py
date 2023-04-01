# lab4.2.3guess2.py
# The program prompts the user to guess a number,
# the program will tell the user if there guess is too high or too low.
# Author: Stefania Verduga

numberToGuess = 30

guess = int(input("Please, guess the number: "))
while guess != numberToGuess:
    if guess < numberToGuess:
        print("too low")
    else:  # I know it can be equal or too low, so it 
    # must be too high
        print("too high")
    guess = int(input("Please, guess again: "))

print("Well done! Yes, the number was", numberToGuess)
