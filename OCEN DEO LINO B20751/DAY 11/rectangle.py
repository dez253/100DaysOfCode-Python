#using a simple function

def calculate_rectangle_area(length, width):
    area = length * width
    return area

#calling the function with argumnents
length = float(input("enter the length of the rectangle"))
width = float(input("enter the width of the rectangle"))

area = calculate_rectangle_area(length, width)
print(f"the area of the rectangle with length{length} and width {width} is {area}")