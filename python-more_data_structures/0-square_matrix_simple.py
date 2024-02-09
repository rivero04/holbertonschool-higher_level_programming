#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    new_matrix = []

    for fila in matrix:
        nueva_fila = []

        for x in fila:
            nueva_fila.append(x**2)
        new_matrix.append(nueva_fila)

    return new_matrix
