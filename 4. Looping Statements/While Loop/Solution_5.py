# Question : Write a program to print sum of all digit. (Ex. -> 145 :- 1 + 4 + 5 = 10)

# Taking input from the user 
num = int(input("Enter the number : "))

sum = 0

# Using while loop to calculate the sum of all numbers
while num > 0 : 
    sum += (num%10)
    num //= 10

# Displaying the sum of all numbers 
print(f"Sum of all numbers : {sum}")