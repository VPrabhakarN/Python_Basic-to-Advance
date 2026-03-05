# Question : Given a list of numbers, use filter() to return only even numbers.

# Defining a list 
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtering even numbers
result = filter(lambda x:x%2==0, nums)

# Displaying the even numbers from the list
print(f"Even Numbers : {list(result)}")