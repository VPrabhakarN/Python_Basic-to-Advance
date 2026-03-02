# Question : Binary Search : Search for a given element.

# Defining the list
numbers = [11, 13, 17, 19, 21, 23, 25, 26, 28, 31, 32, 34, 37, 38, 41, 42]

# Taking an input from the user 
num = int(input("Enter the number : "))

# start & end
start = 0
end = len(numbers)-1

# While loop 
while start <= end :
    mid = (start+end) // 2
    
    if numbers[mid] == num :
        print(f"Number found at {mid} index !")
        break
    elif numbers[mid] < num :
        start = mid+1 
    else :
        end = mid - 1
        
        