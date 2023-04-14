#!/usr/bin/python3
"""This module contains `add_integer` function."""


def add_integer(a, b=98):
    """Add two integers or floats.

    Args:
        a (int/float): Integer or float
        b (int/float): Integer or float

    Returns:
        sum (int): The sum of `a` and `b` rounded to the nearest integer

    """
    if (
        not isinstance(a, int) and not isinstance(a, float)
    ) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if (
        not isinstance(b, int) and not isinstance(b, float)
    ) or isinstance(b, bool):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
