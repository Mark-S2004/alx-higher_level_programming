#!/usr/bin/python3
"""Design and Build a Square class."""


class Square:
    """Sqaure Object.

    Attributes:
        size (int): Square size.

    """

    def __init__(self, size=0):
        """Initialize Square Object instance.

        Args:
            size(int): Square size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
