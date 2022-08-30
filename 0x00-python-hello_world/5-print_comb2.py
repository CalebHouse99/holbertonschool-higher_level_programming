#!/usr/bin/python3

for i in range(0, 100):
    tens = (i % 100) // 10
    ones = i % 10
    if i == 99:
        print("{}".format(i), end="")
    else:
        print("{}{}".format(tens, ones), end=", ")
