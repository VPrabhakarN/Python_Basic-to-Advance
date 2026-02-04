# Question : Write a program to print the table of number accepted from the user.

# Taking number from the user 
num = int(input("Enter the number : "))

# Using for loop to print the table of number accepted from the user 
for i in range (num, (num*11), num) :
    print(i)