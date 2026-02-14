# Defining the function 
def MultiplySquare(a, b):
    # Getting the product of these two values
    product = a * b
    
    # Getting and returning square of product
    return product * product
    

# Taking an inputs from the user 
a = int(input("Enter 1st Value : "))
b = int(input("Enter 2nd Value : "))

# Calling the function 
result = MultiplySquare(a, b)

# Displaying the result
print(result)