# Question : Sum and Average of the tuple.

# Defining a tuple 
numbers = (12, 14, 16, 27, 12, 10, 56, 98)
sum = 0

# Calculating the sum of all elements
for item in numbers :
    sum += item
    
# Displaying the sum and average of the tuple 
print(f"Sum of elements in tuple : {sum}")
print(f"Average of the elements in tuple : {sum//len(numbers)}")