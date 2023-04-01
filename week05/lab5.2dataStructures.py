# lab5.2dataStructures.py
# The program puts 10 random numbers into a queue,
# then, it should output all the values in the queue,
# then take the numbers from the queue, one at a time,
# print it and the current numbers still in the queue.
# Author: Stefania Verduga

import random
queue = []
numberOfNumbers=10
rangeTo=100

for n in range(0,numberOfNumbers):
    queue.append(random.randint(0,rangeTo))

print(f"queue is {queue}")

while len(queue) != 0:

    currentNumber = queue.pop(0)  # the command pop(0) takes the first element out of a list
    print(f"current number is {currentNumber} and the queue is {queue} ")

print("the queue is now empty")
