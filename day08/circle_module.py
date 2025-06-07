import math

def get_radius():
    return float(input("Enter the radius of your circle: "))

def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_circumference(radius):
    return 2 * math.pi * radius

def print_results(area, circumference):
    print(f"The area of your circle is: {area}")
    print(f"The circumference of your circle is: {circumference}")