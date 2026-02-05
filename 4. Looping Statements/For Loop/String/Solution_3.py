# Question : Count the number of vowels in a string using a for loop.

# Taking input from the user
text = input("Enter your string : ")
count = 0

# Using for loop to count total vowels in a string 
for i in text :
    if i == 'a' or i == 'e' or i == 'i' or i =='o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i =='O' or i == 'U' :
        count = count + 1

# Displaying the count of vowels in a string
print(f"Total number of vowels in string : {count}")