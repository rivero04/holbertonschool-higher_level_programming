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
        
    @property
    def size(self):
        """
        Getter for the size of the Square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size of the Square.
        """
        self.width = self.height = value

    def __str__(self):
        """
        Returns a string representation of the Square instance.
        """
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))
