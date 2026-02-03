# Question : Write a program to input any alphabet and check whether it is vowel or consonant.

# Taking input from the user 
ch = input("Enter the character : ")

# Using the if-else statement to check the alphabate is vowel or consonant 
if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch =='E' or ch == 'I' or ch == 'O' or ch == 'U' :
    print(f"{ch} is vowel !")
else :
    print(f"{ch} is consonant !")