#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_number = number % 10
if number < 0:
    last_number = last_number - 10
print(f"Last digit of {number} is {last_number} and is", end=" ")
if last_number == 0:
    print(f"0")
elif last_number > 5:
    print(f"greater than 5")
else:
    print(f"less than 6 and not 0")
