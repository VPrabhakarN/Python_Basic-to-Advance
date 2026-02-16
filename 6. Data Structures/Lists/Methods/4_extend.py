# Defining the list 
a = [10, 20, 30, 40, 50]

# extending the list using 'extend()' method
a.extend([60, 70, 80])
a.extend([90, 100])

# Displaying the list
print(a)

# Iterating the list (Way 1)
for item in a:
    print(item, end=" ")
    
print()

# Iterating the list (Way 2)
for i in range(len(a)) :
    print(a[i], end=" ")
