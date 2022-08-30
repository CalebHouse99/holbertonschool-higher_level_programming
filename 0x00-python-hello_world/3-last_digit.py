#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number % 10
if number < 0 and digit != 0:
    digit = (10 - digit) * -1
if digit > 5:
    last_message = "and is greater than 5"
if digit < 6:
    last_message = "and is less than 6 and not 0"
if digit == 0:
    last_message = "and is 0"
print("Last digit of", number, "is", digit, last_message)
