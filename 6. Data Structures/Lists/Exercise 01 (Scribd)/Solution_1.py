# Question : Write a Python program to sum all the items in a list.

# Defining the list
numbers = [10, 101, 230, 7, 12, 72, 19]

# Calculating the sum of all the items in a list
sum = 0
for number in numbers :
    sum += number
    
# Displaying the sum of all the items in a list
print(f"List : {numbers}")
print(f"Sum of all items in list : {sum}")