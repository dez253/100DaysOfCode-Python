import math
def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cant be negative.")
    return math.pi * radius**2