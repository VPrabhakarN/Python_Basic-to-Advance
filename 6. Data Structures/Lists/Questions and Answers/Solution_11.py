# Question : Selection Sort : Sort the list.

# Defining the list
numbers = [10, 65, 128, 32, 19, 42, 23, 7, 11, 28, 3, 99, 17]

# Printing the list before sorting 
print(f"List before sorting : {numbers}")

# Applying the selection sort technique to sort the list
for i in range(0, len(numbers)-1) :
    min = i
    j = i + 1
    
    for k in range(j, len(numbers)) :
        if numbers[k] < numbers[min] :
            min = k 
            
    numbers[i], numbers[min] = numbers[min], numbers[i]
    
    # Printing the list after sorting
    print(f"List after sorting :  {numbers}")