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
    
    if type(a) is str:
        raise TypeError("a must be an integer")
    
    if type(b) is str:
        raise TypeError("b must be an integer")
        
    
    try:
        inta = int(a)
    except (ValueError, TypeError):
        raise TypeError("a must be an integer")

    try:
        intb = int(b)
    except (ValueError, TypeError):
        raise TypeError("b must be an integer")

    return (inta + intb)

