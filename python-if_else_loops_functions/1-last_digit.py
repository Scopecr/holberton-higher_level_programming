#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number
last_d = abs(number) % 10
if n < 0:
    last_d = -last_d
if last_d > 5:
    print('Last digit of {} is {} and is greater than 5'.format(n, last_d))
elif last_d == 0:
    print("Last digit of {} is {} and is 0".format(n, last_d))
elif last_d < 6 != 0:
    print('Last digit of {} is {} and is less than 6 and not 0'.format(n, last_d))
