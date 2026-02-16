# Defining the list 
a = [10, 20, 30, 40, 50]

# Inserting an element to the list by using the 'insert()' method 
a.insert(0, 5)
a.insert(2, 15)
a.insert(4, 25)
a.insert(6, 35)

# Displaying the list 
print(a)

# Iterating the list (Way 1)
for item in a :
    print(item, end=" ")
    
print()
    
# Iterating the list (Way 2)
for i in range(len(a)) :
    print(a[i], end=" ") 
