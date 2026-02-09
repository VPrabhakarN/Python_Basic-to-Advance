# Question : Write a program to check whether the number is Automorphic number. (Ex. -> Sq of 5 ends with 5, Sq of 25 ends with 25)

# Taking the input from the user 
num = int(input("Enter the number : "))

temp = num 
square = num**num
count = 0

# Using while loop 
while num > 0 :
    count += 1
    num //= 10
    

# Calculation 
extract = square % (10 ** count)

# Using if statement to check the condition 
if extract == temp :
    print("It is an Automorphic Number !")
else :
    print("It is Not an Automorphic Number !")