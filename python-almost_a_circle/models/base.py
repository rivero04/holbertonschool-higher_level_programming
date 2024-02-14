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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.
        """
        if list_objs is None:
            list_dicts = []
        else:
            list_dicts = []
            for obj in list_objs:
                dict_obj = obj.to_dictionary()
                list_dicts.append(dict_obj)

        filename = cls.__name__ + '.json'

        with open(filename, 'w') as file:
            json_string = cls.to_json_string(list_dicts)
            file.write(json_string)

        @staticmethod
        def from_json_string(json_string):
            """
            Returns the list representation of json_string.
            """
            if not json_string:
                return []
            else:
                return json.loads(json_string)
