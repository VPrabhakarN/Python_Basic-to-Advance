# Question : Write a program to find maximum between three numbers.

# Taking input from the user 
num_1 = int(input("Enter the first number : "))
num_2 = int(input("Enter the second number : "))
num_3 = int(input("Enter the third number : "))

# Using if statement to check the condition 
if num_1 > num_2 and num_1 > num_3 :
    print(f"{num_1} is greater than {num_2} and {num_3}")