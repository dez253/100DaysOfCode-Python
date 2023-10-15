#import thee custom module
import circle_area

try:
    #get the user input for the radius
    radius = float(input("Input the raidus of the cicrle:"))
    
    #Calculate the area using the custom module
    area = circle_area.calcu.ate_circle_area(radius)
    
    #display the result
    print(f"the area of the circle with radius {radius} is {area:.2f}")

except ValueError as ve:
    print(f"Error : {ve}. Please enter a valid radius.")
    
except Exception as e:
    print(f"An unexpected error occured : {e}")
    
