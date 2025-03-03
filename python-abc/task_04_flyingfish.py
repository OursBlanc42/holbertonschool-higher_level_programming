#!/usr/bin/python3

"""
Exploring Multiple Inheritance
"""


class Fish:
    """
    Fish : A class representing a fish
    """
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """
    Bird : A class representing a bird
    """
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish (Fish, Bird):
    """
    FlyingFish : A class representing a flying fish
        inherit from Fish and Bird
    """
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
