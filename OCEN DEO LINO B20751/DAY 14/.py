try:
    #get user input for two numbers
    numerator = float(input("Enter the numberator : "))
    denominator = float(input("Enter the denomintor: "))
    
    #Check for the divison by zero
    if denominator == 0:
        raise zero_divison_error("dividing be zero isnt allowed.")
    
    #Perform the divison
    result = numerator / denominator
    
    # show the result
    print(f"Result: {numerator} / {denominator} = {result}")
    
except ValueError as ve:
    #Handle the situatoin where the user may not enter the valid numbers
    print(f"Error: {ve}. Please enter valid numbers.")
    
except zero_divison_error as zde:
    # Handle divison by zero exception
    print(f"Error: {zde}")
except Exception as e:
    print(f"an unexpected error occured: {e}")

finally:
    print("program done well")