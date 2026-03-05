# Question : Given a list of numbers, use map() to square each number.

# Defining a list 
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using map function to square each number present in the list
result = map(lambda x:x**2, nums)

# Displaying the squares
print(f"Squares : {list(result)}")