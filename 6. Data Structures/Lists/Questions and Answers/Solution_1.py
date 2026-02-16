# Taking the size of the list from the user
size = int(input("Enter the size of the list : "))

numbers = []

# For loop to take input from the user
for i in range(0, size) :
    numbers.append(int(input(f"Enter element for {i} index : ")))
    
sum = 0

    
# For loop to calculate the sum and average of element
for number in numbers :
    sum += number
    
# Displaying the sum and average
print(f"Sum of all number present in list : {sum}") 
print(f"Average of all number present in list : {sum//size}") 