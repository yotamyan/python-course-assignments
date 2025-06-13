import math

def calc_area(radius):
    """
    Calculate the area of a circle.

    >>> calc_area(1)
    3.141592653589793
    >>> round(calc_area(2), 2)
    12.57
    """
    return math.pi * radius ** 2

def calc_circumference(radius):
    """
    Calculate the circumference of a circle.

    >>> calc_circumference(1)
    6.283185307179586
    >>> round(calc_circumference(2), 2)
    12.57
    """
    return 2 * math.pi * radius
