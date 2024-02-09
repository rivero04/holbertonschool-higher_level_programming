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

