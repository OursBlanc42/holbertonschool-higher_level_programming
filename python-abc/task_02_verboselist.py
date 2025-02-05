#!/usr/bin/python3

"""
Extending the Python List with Notifications
"""


class VerboseList(list):
    """
    VerboseList Extend python "list" method with verbose

    Args:
        list (list): Input list
    """

    def append(self, item):
        """
        append Improvement with verbose
        """
        try:
            super().append(item)
            print(f"Added [{item}] to the list.")
        except Exception:
            pass

    def extend(self, item):
        """
        extend Improvement with verbose
        display the number of element added
        """
        try:
            super().extend(item)
            print(f"Extended the list with [{len(item)}] items.")
        except Exception:
            pass

    def remove(self, item):
        """
        remove Improvement with verbose
        """
        try:
            print(f"Removed [{item}] from the list.")
            super().remove(item)
        except Exception:
            pass

    def pop(self, item=None):
        """
        pop Improvement with verbose
            Show the index of the element popped
            If no index specified, delete the last one
        """
        if item is None:
            item = len(self)

        try:
            item_incremented = item + 1
            print(f"Popped [{item_incremented}] from the list.")
            super().pop(item)
        except Exception:
            pass
