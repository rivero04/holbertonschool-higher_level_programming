#!/usr/bin/python3
"""
Divide an element of the matrix by a number
"""


def matrix_divided(matrix, div):
    """
    Divides each element of a matrix by a number, returns a new matrix.
    """
    err_msg = ("matrix must be a matrix (list of lists) "
               "of integers/floats")
    if not isinstance(matrix, list):
        raise TypeError(err_msg)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(err_msg)
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(err_msg)

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for item in row:
            new_item = round(item / div, 2)
            new_row.append(new_item)
        new_matrix.append(new_row)

    return new_matrix
