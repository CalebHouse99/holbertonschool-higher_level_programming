#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    print('{}'.format('\n').join(['{}'.format(" ").join([str(cell) for cell in row]) for row in matrix]))
