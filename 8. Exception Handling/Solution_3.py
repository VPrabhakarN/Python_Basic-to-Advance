# Question :  Handle IndexError when accessing list elements.

# Defining a list 
nums = [1, 2, 3, 4, 5, 6]

try :
    for i in range(len(nums)+1) :
        print(nums[i])
        
        
except Exception as error :
    print(f"Error Occupied : {error}")
    
