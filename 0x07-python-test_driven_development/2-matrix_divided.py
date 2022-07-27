#!/usr/bin/python3
""" module on matrix division"""


def matrix_divided(matrix, div):
    """ this function divide each item of
    a matrix by div.
    matrix must not be empty and must be a list.
    div must not be 0, otherwise a ZeroDivisionError is
    give.

    Args:
        matrix(list): must be a list
        div(int, float): must not be 0
    Returns:
        Returns a list of new matrix where each
        item is divided by div
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of "
                            "integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
    return[[round(item / div, 2) for item in row] for row in matrix]
