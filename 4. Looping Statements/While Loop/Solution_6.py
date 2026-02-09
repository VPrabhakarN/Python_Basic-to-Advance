# Question : Write a program to reverse the number.

# Taking the input from the user 
num = int(input("Enter the number : "))

reverse = 0

# Using while loop to reverse the number 
while num > 0 :
    digit = num % 10
    reverse = (reverse*10) + digit
    num //= 10

# Displaying the reverse number 
print(f"Reverse Number : {reverse}")
