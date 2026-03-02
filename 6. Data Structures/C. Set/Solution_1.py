# Question : Symmetric Difference Finder : WAP to find the symmetric difference between two sets.

# Defining method to find the symmetric difference of two sets
def symm_diff(set1, set2) :
    return (set1 ^ set2)

# Defining the set 1 & set 2
set1 = {10, 20, 40, 60}
set2 = {80, 60, 20, 70}

# Calling the method to define the symmetric difference of two sets
print(f"Symmetric Difference : {symm_diff(set1, set2)}")