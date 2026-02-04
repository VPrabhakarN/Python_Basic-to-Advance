# Question : Write a program to find the factorial number.

# Taking the number from the user
num = int(input("Enter the number : "))
fact = 1


# Using for loop to identify the factorial number 
for i in range (1, num, 1) :
    fact = fact + (fact * i)

# Displaying the factorial number
print(f"Factorial of {num} is {fact}.")