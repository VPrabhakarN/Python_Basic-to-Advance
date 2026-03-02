# Question : Find the largest element in the list along with it's index.

# Defining the list 
numbers = [19, 23, 42, 7, 98, 12] 

# Finding the max number
max = numbers[0]
index = 0

for i in range(0, len(numbers)) :
    if numbers[i] > max :
        max = numbers[i]
        index = i
        
# Displaying the max number in the list along with the index number
print(f"List : {numbers}")
print(f"Maximum number in the list is {max} which is at {index} index position!")