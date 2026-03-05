# Question : Given a list of numbers, use map() to convert all numbers to strings.

# Defining a list
nums = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10]

# Copnverting all the numbers to strings
text = map(lambda x:str(x), nums)

# Displaying all converted strings
print(f"Converted Strings : {list(text)}")
