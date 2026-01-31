# Qyestion : Even or Odd Checker -> Accept the number from the user and check whether it's even or odd using modulus.

# Taking input from the user 
num = int(input("Enter a number : "))

# Using elif statement to check the conditions
if num % 2 == 0:
    print(f"{num} is an Even number")
elif num % 2 != 0:
    print(f"{num} is an Odd number")
else:
    print("Invalid Input !!! Please enter a valid number !!")
    

