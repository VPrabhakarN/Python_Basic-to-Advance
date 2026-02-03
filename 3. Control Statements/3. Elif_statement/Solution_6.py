# Question : Write a program to check whether a character is uppercase or lowercase alphabet.

ch = input("Enter a Alphabet : ")

# Using if-elif-else statement to check the condition 
if 'a' <= ch or ch >= 'z' :
    print(f"{ch} is in lower case !")
elif 'A' <= ch or ch >= 'Z' :
    print(f"{ch} is in UPPER LOWER CASE !")
else :
    print(f"{ch} is not alphabet")