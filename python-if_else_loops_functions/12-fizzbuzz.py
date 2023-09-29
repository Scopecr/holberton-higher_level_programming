#!/usr/bin/python3
def fizzbuzz(n):
    result = []
    for i in range(1, 100):
        if i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
    return result
