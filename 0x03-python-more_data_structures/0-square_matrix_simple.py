#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy = [row[:] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            copy[i][j] = copy[i][j] * copy[i][j]
    return copy
