#!/usr/bin/python3

"""
    Module for base_geometry
"""


class BaseGeometry():
    """
    BaseGeometry Improve base geometry with a public instance method
    """
    def area(self):
        """
        area pass

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer_validator Validate the "value" variable

        Args:
            name (string): Name of the value (always a string)
            value (int): Value

        Raises:
            TypeError: Must be an integer
            ValueError: Must be >= 0
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            return True


class Rectangle(BaseGeometry):
    """
    Rectangle Class to create a rectangle based on BaseGeometry

    Args:
        BaseGeometry (class): inheritance
    """
    def __init__(self, width, height):
        """
        __init__ Build the instance of the rectangle

        Args:
            width (any): width of the rectangle
            height (any): height of the rectangle
        """
        a = self.integer_validator("width", width)
        b = self.integer_validator("height", height)
        self.__width = width
        self.__height = height
        print(f"a width = {a}")
        print(f"b height = {b}")
