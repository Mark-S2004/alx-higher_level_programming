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
        self.__size = size

    @property
    def size(self):
        """Get size attribute value."""
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate current square area.

        Returns:
            area (int): Sqaure area

        """
        return self.__size**2

    def my_print(self):
        """Print in stdout the square with the character #."""
        if self.__size:
            for i in range(self.__size):
                print('#' * self.__size)
        else:
            print()
