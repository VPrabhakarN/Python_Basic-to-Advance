# Question : Write a program to check whether a character is alphabet or not.

# Taking the input from the user 
ch = input("Enter character : ")

# Using if-else statement to check whether a character is alphabet or not.
if 'a' <= ch and 'z' >= ch or 'A' <= ch and 'z' >= ch :
    print(ch, " is a alphabet !")