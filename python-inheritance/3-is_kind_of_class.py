#!/usr/bin/python3
"""
    Checks if obj is an instance or subclass.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if obj is an instance of a_class or a subclass of a_class.
    """
    return isinstance(obj, a_class)
