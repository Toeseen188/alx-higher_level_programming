#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    _matrix = []
    for row in matrix:
        new_row = list([i**2 for i in row])
        _matrix.append(new_row)
    return _matrix
