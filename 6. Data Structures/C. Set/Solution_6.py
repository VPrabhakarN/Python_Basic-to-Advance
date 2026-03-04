# Question : Find the symmetric difference of two sets.

def sym_dif (s1, s2) :
    return (s1 ^ s2)

s1 = {1, 3, 5, 6, 7, 8}
s2 = {1, 2, 4, 5, 7, 8, 9}

print(f"Symmetric Difference : {sym_dif(s1, s2)}")