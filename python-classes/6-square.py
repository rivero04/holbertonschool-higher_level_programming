#!/usr/bin/python3
"""
    Create a Square
"""


class Square:
    """
    The Square class defines a square with a given size and position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        This method initializes a Square instance.
        """
        self.size = size  # This will call the setter
        self.position = position  # This will call the setter

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

    @property
    def position(self):
        """
        This is the getter method for position. \
        It returns the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        This is the setter method for position. \
        It sets the position of the square.
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            for i in value:
                if not isinstance(i, int) or i < 0:
                    raise TypeError("position must be a tuple \
                        of 2 positive integers")
            self.__position = value

    def area(self):
        """
        This method calculates and returns the area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        This method prints the square with the character '#'.
        """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
