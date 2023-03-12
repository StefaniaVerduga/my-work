# lab3.2.4convert.py
# This program takes in a float amount of dollars
# and returns that absolute amount in cents
# Author: Stefania Verduga

amountDollars = float(input("Please, enter an amount: "))
# The amount in cents should be an absolute amount and not a float number
# That is why we use int
amountCents = int(abs(amountDollars) * 100)
print('{} in cents is {}'.format(amountDollars, amountCents))
