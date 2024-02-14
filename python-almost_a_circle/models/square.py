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

    def update(self, *args, **kwargs):
        """
        Updates attributes in the order of id, size, x, y.
        """
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

        def to_dictionary(self):
            """
            Returns the dictionary representation of a Square.
            """
            return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
