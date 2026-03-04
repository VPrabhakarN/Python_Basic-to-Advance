# Question : Count frequency of each element in an array/list.

def frequency(nums) :
    dict = {}
    
    for i in nums :
        if i in dict :
            dict[i] += 1
        else :
            dict[i] = 1
            
    return dict

# Defining a list
nums = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 34, 23, 8, 7, 3]

# Printing the frequency of each item
print(f"Frequency of each item : {frequency(nums)}")

     