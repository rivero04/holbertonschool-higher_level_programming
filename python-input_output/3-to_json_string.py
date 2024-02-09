#!/usr/bin/python3
"""
Convert an object.
"""


import json


def to_json_string(my_obj):
    """
    Convert an object to a string representation.
    """
    return json.dumps(my_obj)
