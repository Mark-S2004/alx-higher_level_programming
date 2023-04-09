#!/usr/bin/python3
"""Design and Build a Square class."""


class Square:
    """Sqaure Object.

    Attributes:
        size (int): Square size.
        position (tuple(int)): Square position in 2D

    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize Square Object instance.

        Args:
            size(int): Square size.
            position (tuple(int)): Square position in 2D
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Get size attribute value."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """Get position attribute value."""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Calculate current square area.

        Returns:
            area (int): Sqaure area

        """
        return self.__size**2

    def my_print(self):
        """Print in stdout the square with the character #."""
        if self.__size:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)
        else:
            print()
