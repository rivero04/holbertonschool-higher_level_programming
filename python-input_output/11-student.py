#!/usr/bin/python3
"""
Create class Student
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return the dictionary description for JSON.
        """
        obj_dic = self.__dict__
        serializable_dict = {}
        if attrs is None:
            for key, value in obj_dic.items():
                if isinstance(value, (list, dict, str, int, bool)):
                    serializable_dict[key] = value
        else:
            for attr in attrs:
                if attr in obj_dic:
                    if isinstance(obj_dic[attr], (list, dict, str, int, bool)):
                        serializable_dict[attr] = obj_dic[attr]
        return serializable_dict

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance from a dictionary.
        """
        for key in json:
            if key in self.__dict__:
                self.__dict__[key] = json[key]
