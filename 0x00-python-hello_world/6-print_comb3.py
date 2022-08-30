#!/usr/bin/python3

i = 1

while i < 90:
    tens = (i % 100) // 10
    ones = i % 10
    ones_savepoint = tens + 1
    if tens > 0 and ones == 0:
        ones = ones_savepoint
        i = (tens * 10) + ones
        print("{}{}".format(tens, ones), end=", ")
        i+=1
        continue
    elif i == 89:
        print("{}".format(i), end="\n")
        i+=1
    else: 
        print("{}{}".format(tens, ones), end=", ")
        i+=1
