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
        self.name = name

        if type(value) is not int:
            raise TypeError(f"{self.name} must be an integer")

        self.value = value

        if value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")