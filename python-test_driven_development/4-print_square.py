#!/usr/bin/python3
"""
Prints a square
"""


def print_square(size):
    """
    Print a square of '#' characters.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
