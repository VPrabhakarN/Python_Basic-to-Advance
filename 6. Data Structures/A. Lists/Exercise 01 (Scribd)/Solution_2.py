# Question : Write a Python program to multiply all the items in a list.

# Defining the list
numbers = [1, 2, 3, 4, 5, 7, 9, 3]

# Multiplying the all the elements in a list 
product = 1
for number in numbers :
    product *= number
    
# Displaying the product 
print(f"List : {numbers}")
print(f"Multiplication of all elements : {product}")