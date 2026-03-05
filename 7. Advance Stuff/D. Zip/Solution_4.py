# Question : Use zip() to combine two lists and form sentences.

# Defining two lists 
subjects = ["I ", "You ", "We "]
verbs = ["run", "eat", "study"]

# Combining two lists
result = [x+y for x, y in zip(subjects, verbs)]

# Displaying the result
print(f"Result : {list(result)}")

