#!/usr/bin/python3

"""
Module for basic calculation (add).
"""


def add_integer(a, b=98):
    """
    add_integer : Function that adds 2 integers

    Args:
        a (int): first integer
        b (int, optional): second integer. Defaults to 98.


    """

    if type(a) is float:
        a = int(a)

    if type(b) is float:
        b = int(b)

    if type(a) is not int:
        raise TypeError("a must be an integer")

    if type(b) is not int:
        raise TypeError("b must be an integer")

    return (a + b)
