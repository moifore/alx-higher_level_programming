#!/usr/bin/python3
def safe_print_division(a, b):
    """Returns the division of a and b."""
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
	div = None
    finally:
	print("Inside result: {}".format(result))
    return (div)
