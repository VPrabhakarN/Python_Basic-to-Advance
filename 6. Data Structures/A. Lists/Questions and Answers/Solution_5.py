# Question : Left Rotation by 1 -> Shift all the elements one position to the left, with the first element moving to end.

# Defining the list
numbers = [10, 20, 30, 40, 50]

print(f"List before : {numbers}")

# Shifting all the elements one position to the left
for i in range(0, len(numbers)-1) :
    numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
    
# Displaying the result
print(f"List after : {numbers}")