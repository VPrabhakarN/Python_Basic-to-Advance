# Question : Write a program to check whether the number is Palindrome number.

# Taking the input from the user 
num = int(input("Enter the number : "))

temp = num
sum = 0

# Using while loop 
while temp > 0 :
    digit = temp%10
    sum = (sum*10) + digit
    temp //= 10

# Using if conndition to check the number is palindrome or not 
if num == sum :
    print("Palindrome Number!")
else :
    print("It's not Palindrome Number!")