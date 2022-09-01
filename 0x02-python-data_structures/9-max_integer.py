#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    biggest = -1
    for i in range(0, len(my_list)):
        if my_list[i] > biggest:
            biggest = my_list[i]
    return biggest
