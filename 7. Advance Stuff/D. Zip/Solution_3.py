# Question : Using zip(), create a new list containing the sum of elements at the same index.

# Defining a lists
a = [10, 20, 30]
b = [1, 2, 3]

# Performing sum operation 
result = [x+y for x,y in zip(a, b)]

# Displaying the result
print(f"Result : {list(result)}")