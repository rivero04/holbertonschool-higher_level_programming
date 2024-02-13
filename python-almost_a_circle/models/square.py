#!/usr/bin/python3
"""Create Class Base"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor of the Square class.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the Square instance.
        """
        return ("[Square] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width))
