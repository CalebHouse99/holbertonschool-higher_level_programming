#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    newple = []
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    for i in range(0, len(tuple_a)):
        if len_a < 2:
            tuple_a += (0,)
        if len_b < 2:
            tuple_b += (0,)
        newple.append(tuple_a[i]+tuple_b[i])
    newple = tuple(newple)
    return newple
