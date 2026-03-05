# Question : Given a list of numbers, return True if number is even else False using map().

def even(x) :
    if x%2 == 0 :
        return True
    else :
        return False

# Defining a list 
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14]

# Checking each number whether it is even or not 
result = map(even, nums)

# Displaying the result 
print(f"Result : {list(result)}")

