# Question : Check the list is sorted or not.

# Defining an list 
numbers = [12, 19, 23, 42, 48, 77, 81, 89, 99]

# Displaying the list
print(f"List : {numbers}")

# Checking whether the list is sorted or not 
for i in range(0, len(numbers)-1) :
    if numbers[i] < numbers[i+1] :
        continue
    else :
        print("List is Not Sorted!!")
        break
else :
    print("List is Sorted!!!!")