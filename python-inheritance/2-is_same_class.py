#!/usr/bin/python3
"""
    Checks if obj is an instance of a_class
"""


def is_same_class(obj, a_class):
    """
    Checks if obj is an instance of a_class.
    """
    return type(obj) is a_class
