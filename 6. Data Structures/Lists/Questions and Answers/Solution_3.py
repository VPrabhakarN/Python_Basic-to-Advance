# Question : Find the 2nd largest element in the list along with it's index.

# Defining the list 
numbers = [10, 89, 23, 12, 19, 42]

# Finding 2nd max number
max1 = numbers[0]
max2 = numbers[0]
index1 = 0
index2 = 0

for i in range (0, len(numbers)) :
    if numbers[i] > max1 :
        max2 = max1
        max1 = numbers[i]
        index2 = index1
        index1 = i
        
    elif numbers[i] > max2 and numbers[i] != max1:
        max2 = numbers[i]
        index2 = i
        
# Displaying the 2nd max number along with the index
print(f"List : {numbers}")
print(f"2nd Highest Value in the List : {max2}")