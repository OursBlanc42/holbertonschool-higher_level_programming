#!/usr/bin/python3

"""
This module contains the definition of class 'Rectangle'
"""


class Rectangle:
    """
    Class to define a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        __init__ Constructor to build the instance_

        Args:
            width (int, optional): Rectangle width. Defaults to 0.
            height (int, optional): Rectangle high. Defaults to 0.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        width Get the width of the rectangle

        Returns:
            int: size of the rectangle (width length)
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        width Define the width of the rectangle

        Args:
            value (int): size of the rectangle (width length)

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def heigh(self):
        """
        heigh Get the heigh of the rectangle

        Returns:
            int: size of the rectangle (heigh length)
        """
        return (self.__heigh)

    @heigh.setter
    def heigh(self, value):
        """
        heigh Define the heigh of the rectangle

        Args:
            value (int): size of the rectangle (height length)

        Raises:
            TypeError: heigh must be an integer
            ValueError: heigh must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("heigh must be an integer")
        if value < 0:
            raise ValueError("heigh must be >= 0")
        self.__heigh = value
