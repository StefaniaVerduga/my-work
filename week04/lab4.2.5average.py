# lab4.2.5average.py
# This program reads in numbers until 
# the user enters 0
# it will them print back out again
# and their average

numbers = []

# first number then we check if it is 0 in the while loop
number = int(input("Enter number (0 to quit): "))

while number != 0:
    numbers.append(number)

    # read the text number and check if 0
    number = int(input("Enter another (0 to quit): "))

for value in numbers:
    print (value)

# I want average to be float
average = float(sum(numbers)) / len(numbers)
print(f"The average is {average}")
