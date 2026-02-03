# Question : Write a program to check whether a year is leap year or not.

# Taking input from the user 
year = int(input("Enter the year : "))

# Using the if else statement to check the year is leap or not 
if year%4 == 0 :
    print(f"{year} is leap year!")
else :
    print(f"{year}, is not leap year!")