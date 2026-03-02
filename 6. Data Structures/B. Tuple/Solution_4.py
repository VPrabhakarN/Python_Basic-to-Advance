# Question : Check the element exist or not.

# Defining a function
def find_element(nums, search) :
    if search in nums :
        return f"{search} Found!"
    else : 
        return f"{search} Not Found!"


# Defining a tuple 
numbers = (1, 4, 6, 7, 8, 10, 11, 15, 16, 19,20, 22, 29, 34, 39, 47, 54)

# Taking an input from the user
to_search = int(input("Enter the number to check whether it exists or not : "))

# Calling the function to check whether the number exists of not
print(f"Your Number : {find_element(numbers, to_search)}")
