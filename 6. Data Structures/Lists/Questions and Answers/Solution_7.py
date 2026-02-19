# Question : Reverse the list (In-Place) : Reverse the entire list without using extra space (i.e., swap elements).

# Defining a list 
numbers = [10, 13, 12, 32, 45, 19]

print(f"List Before : {numbers}")

# Reversing the list
num = len(numbers)-1

for i in range (len(numbers)//2) :
    numbers[i], numbers[num] = numbers[num], numbers[i]
    num -= 1
    
print(f"List After : {numbers}")