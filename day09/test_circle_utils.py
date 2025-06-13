from circle_utils import calc_area, calc_circumference
import math

def test_area():
    assert calc_area(1) == math.pi
    assert round(calc_area(2), 2) == 12.57

def test_circumference():
    assert calc_circumference(1) == 2 * math.pi
    assert round(calc_circumference(2), 2) == 12.57
