#!/usr/bin/python3
"""pascals triangle"""


def pascal_triangle(n):
    """creates a pascals triangle"""

    if n <= 0:
        return ([])
    list = [[1]]
    first_list = []
    for x in range(1, n):
        second_list = [1]
        for j in range(len(first_list) - 1):
            second_list.append(first_list[j] + first_list[j + 1])
        second_list.append(1)
        list.append(second_list)
        first_list = second_list
    return (list)
