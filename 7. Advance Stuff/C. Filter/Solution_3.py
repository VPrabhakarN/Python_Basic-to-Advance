# Question : Return only negative numbers from a list.

# Defining a function to filter 
def negativeornot(x) :
    if x < 0 :
        return x

# Defining a list 
nums = [4,-2,7,-8,-1,3]

# Filtering the negative numbers from the list
result = filter(negativeornot, nums)

# Displying the result
print(f"Negative Numbers : {list(result)}")