# Question : Print Hollow Square Star Pattern.

"""
*****
*   *
*   *
*****
"""

l = 5

# Using for loop to print the 'Hollow square star pattern'
for i in range(0, l) :
    for j in range(0, l):
        if i==0 or i == l-1 or j == 0 or j == l-1 :
            print("*", end="")
        else :
            print(" ", end="")
    print()
