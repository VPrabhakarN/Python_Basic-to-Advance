# Question : Write a program to display the product of the digits of a number accepted from the user.

# Taking input from the user 
number = input("Enter the number : ")
product = 1

# Using for loop to get the product of the digit of a number accepted from the user 
for digit in number :
    product = product * int(digit)

# Displaying the product of the digit of the number accepted from the user
print(f"Product of {number} is {product}.")

