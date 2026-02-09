# Question : Write a program to print each digit in reverse order. (Ex. -> 145 :- 5, 4, 1)

# Taking input from the user 
num = int(input("Enter the number : "))

# Usng while loop to print digit in reverse order 
while num > 0 :
    print(num%10)
    num //= 10
    