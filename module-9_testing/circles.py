from math import pi


def circle_area(r):
    # make sure value errors are raised when necessary
    if r < 0:
        raise ValueError("Tha radius cannot be negative.")

    # make sure type errors are raised when necessary
    if type(r) not in [int, float]:
        raise TypeError("The radius must be a non-negative real number")

    return pi*(r**2)