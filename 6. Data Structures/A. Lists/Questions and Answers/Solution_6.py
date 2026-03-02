# Question : Right Rotation by 1 : Shift all the elements one position to the right, with the first element moving to end.

# Defining the list
numbers = [10, 20, 30, 40, 50]

print(f"List before : {numbers}")

# Shifting all the elements one position to the right
for i in range(len(numbers)-1, 0, -1) :
    numbers[i], numbers[i-1] = numbers[i-1], numbers[i]
    
# Displaying the result
print(f"List after : {numbers}") 