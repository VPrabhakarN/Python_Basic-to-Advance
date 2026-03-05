# Question : Given two lists, create tuples only when sum of pair > 10.

# Defining two lists 
a = [2,6,4,8]
b = [5,3,7,4]

# Filtering the result 
result = (x+y for x,y in zip(a, b) if x+y > 10)

# Displying the result 
print(f"Result : {tuple(result)}")