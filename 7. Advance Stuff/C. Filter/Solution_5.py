# Question : Return numbers divisible by 3.

# Defining a list 
nums = [3,7,9,10,12,18,19,21,23,24,16]

# Filtering the numbers
result = filter(lambda x:x%3==0, nums)

# Displaying the result 
print(f"Result : {list(result)}")
