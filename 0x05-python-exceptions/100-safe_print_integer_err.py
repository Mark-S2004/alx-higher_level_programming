#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as e:
        stderr.write("Exception: " + str(e) + "\n")
        return False
    return True
