#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    print('{}'.format('\n').join([' '.join([str(cell) for cell in row]) for row in matrix]))
