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

    def _is_valid_operand(self, other):
        """Check if `other` can be compared with `Square` object."""
        return hasattr(other, "area")

    def __eq__(self, other):
        """Check if the area of this `Square` is equal to other `Square`.

        Args:
            other (Square): Square object
        """
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if the area of this `Square` is not equal other `Square`.

        Args:
            other (Square): Square object
        """
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if the area of this `Square` is lower than other `Square`.

        Args:
            other (Square): Square object
        """
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.area() < other.area()

    def __le__(self, other):
        """Check if the area of this `Square` is <= other `Square`.

        Args:
            other (Square): Square object
        """
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if the area of this `Square` is greater than other `Square`.

        Args:
            other (Square): Square object
        """
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if the area of this `Square` is >= other `Square`.

        Args:
            other (Square): Square object
        """
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.area() >= other.area()

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
