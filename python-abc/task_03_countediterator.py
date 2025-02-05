#!/usr/bin/python3

"""
Extending the Python Iter method
"""


class CountedIterator:
    """
    VerboseList Extend python "list" method with verbose

    Args:
        list (list): Input list
    """

    def __init__(self, data):
        self.counter = 0
        self.item = iter(data)

    def get_count(self):
        return (self.counter)

    def __next__(self):
        for item in self.item:
            continue
        self.counter += 1
        return self.counter

data = [1, 2, 3, 4]
counted_iter = CountedIterator(data)

try:
    while True:
        item = next(counted_iter)
        print(f"Got {item}, total {counted_iter.get_count()} items iterated.")
except StopIteration:
    print("No more items.")
