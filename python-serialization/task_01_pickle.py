#!/usr/bin/python3
"""
    serialize and deserialize custom Python objects using the pickle module
"""

import pickle


class CustomObject:
    """
     Define a custom object
    """

    def __init__(self, name, age, is_student):
        """
        __init__ constructor

        Args:
            name (string): name of the user
            age (int): age of the user
            is_student (bool): true / false if is a student
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        display
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        serialize with pickle

        Args:
            filename (string): filename

        Returns:
            _type_: _descrption_
        """
        try:
            with open(filename, "wb") as myfile:
                pickle.dump(self, myfile)
        except (FileNotFoundError, IOError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        deserialize abstract method to deserialize with

        Args:
            filename (_type_): _description_

        Returns:
            _type_: _description_
        """
        try:
            with open(filename, "rb") as myfile:
                loaded_data = pickle.load(myfile)
            return loaded_data
        except (FileNotFoundError, IOError, pickle.PickleError):
            return None
