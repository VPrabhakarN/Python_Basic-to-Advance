# Question :  Given a list of strings, return words whose length is greater than 4.

# Defining a list 
text = ["cat","apple","dog","banana", "ani", "vinnyyy", "tanurani"]

# Filtering the strings
result = filter(lambda x:len(x)>4, text)

# Displying the result 
print(f"Result : {list(result)}")

