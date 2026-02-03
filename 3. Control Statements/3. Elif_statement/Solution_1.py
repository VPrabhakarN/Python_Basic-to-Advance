# Question : Compare two numbers -> Take two user inputs and determine which number is greater 

# Taking input from the user 
num1 = int(input("Enter the first number : "  ))
num2 = int(input("Enter the second number : "  ))

# Using elif statement to check the conditions
if num1 > num2:
    print(f"{num1} is greater than {num2}")

elif num2 > num1:
    print(f"{num2} is greater than {num1}")     

else:
    print("Both numbers are equal")



