#!/usr/bin/python3
"""Create Class Base"""


class Base:

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Assigns id if provided, else increments __nb_objects.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
