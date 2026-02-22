# Question : Bubble Sort : Sort the list.

# Defining the list
numbers = [10, 19, 8, 42, 23, 65, 19, 72, 7, 11]

# Printing the list before the sort
print(f"Unsorted List {numbers}")

# Applying the bubble sort technique to sort the list
for i in range (0, len(numbers)-1) :
    for j in range(0, len(numbers)-1) :
        if numbers[j] > numbers[j+1] :
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
            
# Printing the sorted list 
print(f"Sorted List : {numbers}")