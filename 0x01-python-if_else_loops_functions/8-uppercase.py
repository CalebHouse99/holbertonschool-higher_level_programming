#!/usr/bin/python3


def uppercase(str):
    for i in range(0, len(str)):
        current_int = ord(str[i])
        if current_int > 96 and current_int < 123:
            current_int = current_int - 32
        print(chr(current_int), end="")
    print('')
