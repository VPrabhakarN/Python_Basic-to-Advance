# Question : Use zip() to create a dictionary from two lists.

# Defining two lists
keys = ["id", "name", "salary"]
values = [101, "Vijay", 50000]

# Creating a dictionary from two lists
result = zip(keys, values)

# Displying the result 
print(f"Result : {dict(result)}")

