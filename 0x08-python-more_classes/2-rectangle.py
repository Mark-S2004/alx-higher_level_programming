#!/usr/bin/python3
"""This module contains a Rectangle class."""


class Rectangle:
    """Define a rectangle.

    Attributes:
        width (int): Rectangle width
        height (int): Rectangle height

    """

    @property
    def width(self):
        """Get width private instance attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height private instance attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __init__(self, width=0, height=0):
        """Instantiate a `Rectangle` object.

        Args:
            width (int): Rectangle width
            height (int): Rectangle height
        """
        self.width = width
        self.height = height

    def area(self):
        """Calculate the `Rectangle` area.

        Returns:
            area (int): Area of `Rectangle`

        """
        return self.width * self.height

    def perimeter(self):
        """Calculate the `Rectangle` perimeter.

        Returns:
            perimeter (int): Perimeter of `Rectangle`

        """
        if self.__width and self.__height:
            return 2 * self.width + 2 * self.height
        return 0
