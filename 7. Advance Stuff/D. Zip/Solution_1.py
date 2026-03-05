# Question : You are given two lists. Use zip() to combine them into a list of tuples.

# Defining two lists
names = ["Vijay", "Rahul", "Amit"]
ages = [22, 24, 21]

# Combining them into lists of tuples
result = zip(names, ages)

# Displying the result
print(f"Result : {list(result)}")