#!/usr/bin/python3
"""
This module contains a class
with public instance and Raises
exception when required
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry (7-base_geometry.py)
    Arguments:
        BaseGeometry {class} -- super class
    """

    def __init__(self, width, height):
        """Rectangle with private height and width
        Arguments:
            width {int} -- Width of  the rectangle
            height {int} -- Height of  the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
