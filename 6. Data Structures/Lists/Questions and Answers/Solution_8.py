# Question : Linear Search -> Search for a given element by checking each element one by one.

# Defining the list 
numbers = [47, 12, 89, 33, 56, 21, 78, 90, 14, 65]

# Taking an input from the user
num = int(input("Enter the number you want to check : "))

# For loop to perform linear search 
for i in range(len(numbers)) :
    if numbers[i] == num :
        print(f"{num} found in the list!!!!")
        break
else :
    print(f"{num} is not found in the list!!!")