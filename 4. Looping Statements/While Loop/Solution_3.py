# Question : Write a program to calculate the sum of the first N natural numbers.

# Taking the input from the user 
n = int(input("Enter the number : "))
s = 1
sum = 0

# Using while loop to calculate the sum of the first N natural numbers
while s <= n :
    sum += s
    s += 1

# Displaying the sum of natural numbers
print(f"The sum of Natural numbers up to {n} : {sum}")


