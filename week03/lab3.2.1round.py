# lab3.2.1round.py
# We are rounding a number
# It rounds to the nearest even number
# eg 4.5 rounds to 4
# but 5.5 rounds to 6
# Author: Stefania Verduga 

numberToRound = float(input("Enter a float number: "))
roundedNumber = round(numberToRound)
print('{} rounded is {}'.format(numberToRound,roundedNumber))
