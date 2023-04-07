#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        print("Inside result: ", end="")
        result = a / b
    except Exception:
        result = None
    finally:
        print("{}".format(result))
    return result
