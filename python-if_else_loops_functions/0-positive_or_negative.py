#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("The number is greater than 0:", number)
elif number == 0:
    print("The number is 0:", number)
elif number < 0:
    print("The number is less than 0:", number)
