#!/usr/bin/python3

for i in range(00, 100):
    x = '00'
    if i < 10:
        print("{}{}".format(0, i), end=", ")
    elif i == 99:
        print("{}".format(i), end="")
    else:
        print("{}".format(i), end=", ")
