#!/usr/bin/python3
""" Is it inherited
"""


def inherits_from(obj, a_class):
    """ Returns obj or false
    """
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
