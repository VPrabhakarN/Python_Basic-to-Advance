# Question : Return numbers greater than 10 from a list.

# Defining a function to filter
def greaterthan10(x) :
    if x > 10 :
        return x

# Defining a list 
nums = [11, 23, 1, 4, 6, 18, 9, 4, 19, 87, 32, 41, 2, 3, 62, 6, 7, 8]

# Filtering the numbers greater than 10
result = filter(greaterthan10, nums)

# Displaying the result 
print(f"Numbers are greater than 10 : {list(result)}")