#!/usr/bin/python3
"""
Create class Student
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Return the dictionary description for JSON serialization.
        """
        obj_dict = self.__dict__
        serializable_dict = {}
        for key, value in obj_dict.items():
            if isinstance(value, (list, dict, str, int, bool)):
                serializable_dict[key] = value
        return serializable_dict
