#!/usr/bin/python3
"""
    Checks if obj is an instance of a class that inherited
"""


def inherits_from(obj, a_class):
    """
    Checks if obj is an instance of a class that inherited from a_class.
    """
    is_subclass = issubclass(type(obj), a_class)

    is_not_same_class = type(obj) is not a_class

    return is_subclass and is_not_same_class
