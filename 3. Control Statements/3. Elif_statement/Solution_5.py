# Question : Write a program to input any character and check whether it is alphabet, digit or special character.

# Taking the input from the user 
ch = input("Enter the value : ")

# Using If-else statement to check the condition 
if (ch >= 'a' or ch <= 'z') or (ch >= 'A' or ch <= 'Z') :
    print(f"{ch} is a alphabet !!")
elif '0' <= ch >= '9' :
    print(f"{ch} is a digit !")
else :
    print(f"{ch} is a special character !")