# Question : Find the most frequent element in an array/list.

def frq(nums) :
    dict = {}
    
    for i in nums :
        if i in dict :
            dict[i] += 1
        else :
            dict[i] = 1
           
    max = 0 
    ele = 0
    for i in dict :
        if dict[i] > max :
            max = dict[i]
            ele = i
            
            
    return f"Element : {ele} & Frequency : {max}"

# Defining the list 
nums = [1, 2, 2, 3, 4, 2, 5, 5, 6, 7, 7, 9, 20, 12, 13, 14, 11]

# Printing the most frequency element in the list
print(f"Most Frequent Element : {frq(nums)}")

