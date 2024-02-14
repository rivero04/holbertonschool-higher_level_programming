#!/usr/bin/python3
"""Create Class Base"""


import json


class Base:
    """
    Manages id attribute for future classes.
    """
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
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.
        """
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
