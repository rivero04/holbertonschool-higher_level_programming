#!/usr/bin/python3
"""
    Create a Square
"""


class Square:
    """
    The Square class defines a square with a given size.
    """

    def __init__(self, size=0):
        """
        This method initializes a Square instance.
        """
        self.size = size  # This will call the setter

    @property
    def size(self):
        """
        This is the getter method for size. It returns the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This is the setter method for size. It sets the size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        This method calculates and returns the area of the square.
        """
        return self.__size * self.__size
