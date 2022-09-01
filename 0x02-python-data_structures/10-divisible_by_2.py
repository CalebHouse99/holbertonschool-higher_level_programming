#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    booleans = my_list.copy()
    for i in range(0, len(booleans)):
        if booleans[i] % 2 == 0:
            booleans[i] = True
        else:
            booleans[i] = False
    return booleans
