# Square Star Pattern
"""
*****
*****
*****

"""

# Taking value from the user 
rows = int(input("Enter the number of rows : "))
colomn = int(input("Enter the number of coloms : "))

for i in range(0, rows, 1) :
    for j in range(0, colomn, 1) :
        print("*", end=" ")
    print()
    