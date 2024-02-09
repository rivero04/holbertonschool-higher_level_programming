#!/usr/bin/python3
"""
Return the dictionary description for JSON serialization
"""


def class_to_json(obj):
    """
    Return the dictionary description for JSON serialization of an object.
    """
    obj_dict = obj.__dict__
    serializable_dict = {}
    for key, value in obj_dict.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_dict[key] = value
    return serializable_dict
