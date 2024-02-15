#!/usr/bin/python3
"""Create Class Base"""


import json
import os


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

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list representation of json_string.
        """
        if not json_string:
            return []
        else:
            return json.loads(json_string)

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

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances.
        """
        filename = cls.__name__ + '.json'

        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as file:
            json_string = file.read()
        list_dicts = cls.from_json_string(json_string)

        instances = []
        for dict_obj in list_dicts:
            instance = cls.create(**dict_obj)
            instances.append(instance)
        return instances
