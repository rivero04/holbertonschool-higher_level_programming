#!/usr/bin/python3
"""
Convert a string.
"""


import json


def from_json_string(my_str):
    """
    Convert a string to an object.
    """
    return json.loads(my_str)
