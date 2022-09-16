#!/usr/bin/python3
""" mylist inherited from list
"""


class MyList(list):
    """ Class of MyList
    """
    def __init__(self):
        """ initializes MyList
        """
        super().__init__()

    def print_sorted(self):
        """ Prints the list sorted
        """
        print(sorted(self))
