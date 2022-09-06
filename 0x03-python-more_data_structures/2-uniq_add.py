#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    uniques = []
    for i in range(len(my_list)):
        if my_list[i] not in uniques:
            uniques.append(my_list[i])
            total += my_list[i]
    return total
