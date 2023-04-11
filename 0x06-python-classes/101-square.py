#!/usr/bin/python3
"""Design and Build a Square class."""


class Square:
    """Sqaure Object.

    Attributes:
        size (int): Square size.
        __position (tuple(int)): Square __position in 2D

    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize Square Object instance.

        Args:
            size(int): Square size.
            __position (tuple(int)): Square __position in 2D
        """
        self.size = size
        self.position = position
    
    def __str__(self):
        """Return string of the square represented by '#'."""
        string = ""
        if self.size:
            for _ in range(self.position[1]):
                string += "\n"
            for _ in range(self.size):
                string += " " * self.position[0] + "#" * self.size + "\n"
        return string[:-1]

    @property
    def size(self):
        """Get size attribute value."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get __position attribute value."""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if not isinstance(i, int) or i < 0:
                raise TypeError(
                            "position must be a tuple of 2 positive integers"
                            )
        self.__position = value

    def area(self):
        """Calculate current square area.

        Returns:
            area (int): Sqaure area

        """
        return self.size**2

    def my_print(self):
        """Print in stdout the square with the character #."""
        print(self)
