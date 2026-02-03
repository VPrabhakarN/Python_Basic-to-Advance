# Question : Write a program to check whether a number is divisible by 5 and 11 or not.

# Taking input from the user 
num = int(input("Enter the number : "))

if num%5 == 0 and num%7 == 0 :
    print(f"{num} is divisible by 5 and 11")

