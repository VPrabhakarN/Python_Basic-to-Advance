# Question : Remove elements from the tuple.

# Defining a function 
def remove_element(numbers, to_remove) :
    # Converting a tuple into list
    nums = list(numbers)
    nums.remove(to_remove)
    
    # Converting a list into tuple
    numbers = tuple(nums)
    
    # Returning a tuple
    return numbers


# Taking an input from the user 
size = int(input("Enter the size : "))

nums = []

# Taking the values from the user 
for i in range(0, size) :
    num = int(input("Enter the values : "))
    nums.append(num)

numbers = tuple(nums)

# Taking the value to be removed
to_remove = int(input("Enter the value to be removed : ")) 

# Calling the funtion to remove the value
print(f"Tuple before removing element : {numbers}")
print(f"Tuple after removing element : {remove_element(numbers, to_remove)}")   