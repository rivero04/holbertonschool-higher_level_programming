#!/usr/bin/python3
"""
Returns a list of the available attributes and methods.
"""


def lookup(obj):
    """
    Returns a list of the available attributes and methods of an object.
    """
    return dir(obj)
