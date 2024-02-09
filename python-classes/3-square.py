#!/usr/bin/python3
"""
This is the module docstring. This module contains a definition of a Square.
"""


class Square:
    """
    This is the class docstring. The Square class defines a square with a size.
    """

    def __init__(self, size=0):
        """
        This is the method docstring. This method initializes a Square instance
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size  # Private instance attribute

    def area(self):
        """
        This method calculates and returns the area of the square.
        """
        return (self.__size * self.__size)
