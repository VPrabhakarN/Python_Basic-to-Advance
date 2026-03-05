# Question : Convert a list of strings to uppercase using map().

# Defining a list 
text = ["vijay", "vishal", "aniket", "sagar", "nikhil"]

# Converting to uppercase
result = map(lambda x:x.upper(), text)

# Displaying all uppercase strings
print(f"Uppercase string : {list(result)}")