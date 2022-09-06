#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    if type(roman_string) != str:
        return 0
    if len(roman_string) < 1:
        return 0
    for i in range(len(roman_string)):
        current = roman_string[i]
        if len(roman_string) > i + 1:
            next_let = roman_string[i + 1]
            if current == "I" and (next_let != "V" and next_let != "X"):
                num += 1
            elif current == "I" and (next_let == "V" or next_let == "X"):
                num -= 1
            elif current == "V":
                num += 5
            elif current == "X" and (next_let != "L" and next_let != "C"):
                num += 10
            elif current == "X" and (next_let == "L" or next_let == "C"):
                num -= 10
            elif current == "L":
                num += 50
            elif current == "C" and (next_let != "D" and next_let != "M"):
                num += 100
            elif current == "C" and (next_let == "D" or next_let == "M"):
                num -= 100
            elif current == "D":
                num += 500
            elif current == "M":
                num += 1000
        else:
            if current == "I":
                num += 1
            elif current == "V":
                num += 5
            elif current == "X":
                num += 10
            elif current == "L":
                num += 50
            elif current == "C":
                num += 100
            elif current == "D":
                num += 500
            elif current == "M":
                num += 1000
    return num
