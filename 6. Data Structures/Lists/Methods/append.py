# Defining list
a = [10, 20, 30, 40, 50]

# Appending elements to the list by using 'append()' method
a.append(60)

# Displaying the list 
print(a)

# Iterating the list (1st way)
for item in a :
    print(item, end=", ")
    
print()
    
# Iterating the list (2nd way)
for i in range(len(a)) :
    print(a[i], end=", ")