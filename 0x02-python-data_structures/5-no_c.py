#!/usr/bin/python3
def no_c(my_string):
    copy = ""
    for i in range(0, len(my_string) - 1):
        if my_string[i] == "C" or my_string[i] == "c":
            continue
        else:
            copy = copy + my_string[i]
    return copy
