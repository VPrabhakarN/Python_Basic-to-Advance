# Write a program to print even numbers up to a user-defined number N.

# Taking input from the user 
n = int(input("Enter the number (Up to print even numbers) :"))
s = 1

# Using the While loop  to print even numbers 
while s <= n :
    if s%2 == 0 :
        print(s)
        s += 1
    else :
        s += 1
        pass
