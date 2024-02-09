#!/usr/bin/python3
"""
In this module, the class MyList is defined.
"""


class MyList(list):
    """
    This class inherits list.
    """
    def print_sorted(self):
        """
        This method prints the list sorted.
        """
        print(sorted(self))
