#!/usr/bin/python3
"""
Generate Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to n rows.
    """
    if n <= 0:
        return []
    triangle = [[1]]

    for i in range(1, n):
        last_row = triangle[-1]
        new_row = [1]

        for j in range(1, i):
            new_value = last_row[j-1] + last_row[j]
            new_row.append(new_value)

        new_row.append(1)
        triangle.append(new_row)

    return triangle
