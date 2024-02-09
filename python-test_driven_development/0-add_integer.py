#!/usr/bin/python3
"""
This is the addition module.
"""


def add_integer(a, b=98):
    """
    Returns the addition of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
