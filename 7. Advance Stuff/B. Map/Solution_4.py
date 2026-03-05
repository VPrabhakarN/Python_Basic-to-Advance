# Question : Given a list of numbers, use map() to add 10 to every number.

# Defining a list 
nums = [12, 23, 34, 45, 56, 67, 78, 89, 11, 22, 33, 44, 55, 66, 77, 88]

# Adding 10 to every number present in the list
result = map(lambda x:x+10, nums)

# Displaying the answers
print(f"List after adding 10 to each number : {list(result)}")