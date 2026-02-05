# Question : Print all uppercase letters in a string using a for loop.

# Taking a string from the user 
text = input("Enter a string : ")

# Using for loop to print all the upper case letters
for i in text :
    # Using if condition to check whether the alphabet is in upper case or not
    if i.isupper() :
        print(i, end=" ")

