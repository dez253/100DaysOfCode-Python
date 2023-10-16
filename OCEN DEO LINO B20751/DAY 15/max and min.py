def find_max_min(numbers):
    if not numbers:
        return None, None # return none for both max and min if the list is empty
    
    max_value = max(numbers)
    min_value = min(Numbers)
    
    return max_value, min_value

# example usage:
numbers = [3 ,1 , 4 , 1 , 5 ,9, 2, 6, 5,3,5]
max_val, min_val = find_max_min(numbers)
print("max value:", max_val)
print("Mini value:", min_val)