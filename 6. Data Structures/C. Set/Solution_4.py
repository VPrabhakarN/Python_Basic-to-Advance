# Question : Find the intersection of two sets.

def inter_section (s1, s2) :
    return (s1&s2)

s1 = {1, 2, 4, 3, 9, 7}
s2 = {2, 3, 4, 6, 8} 

print(f"Intersection of two sets : {inter_section(s1, s2)}")