#!/usr/bin/python3
"""Class MyInt
"""


class MyInt(int):
    """invert a value
    """

    def __init__(self, value):
        """Initialize value
        """
        self.value = value

    def __eq__(self, other):
        """__eq__ represent a==b
        """
        return self.value != other

    def __ne__(self, other):
        """__ne__ represent a != b
        """
        return self.value == other