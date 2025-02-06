#!/usr/bin/python3

"""
Extending the Python List with Notifications
"""


class VerboseList(list):
    """
    VerboseList Class inherit from the built in list class

    Args:
        list (class): original list class
    """
    def append(self, item):
        """
        append Improve append message with verbose

        Args:
            item (any): item to append
        """
        try:
            super().append(item)
            print(f"Added [{item}] to the list.")
        except Exception:
            pass

    def extend(self, item):
        """
        extend Improve extend message with verbose

        Args:
            item (any): item to extend
        """
        try:
            super().extend(item)
            print(f"Extended the list with [{len(item)}] items.")
        except Exception:
            pass

    def remove(self, item):
        """
        remove Remove extend message with verbose

        Args:
            item (any): item to remove
        """
        try:
            print(f"Removed [{item}] from the list.")
            super().remove(item)
        except Exception:
            pass

    def pop(self, index=-1):
        """
        pop Pop extend message with verbose

        Args:
            index (int, optional): Number of the index to pop.
            Defaults to None.
        """

        try:
            print(f"Popped [{self[index]}] from the list.")
            super().pop(self[index])
        except Exception:
            pass
