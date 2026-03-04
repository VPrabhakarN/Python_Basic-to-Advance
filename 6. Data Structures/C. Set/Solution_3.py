# Question : Find the union of two sets.

def union(s1, s2) :
    return (s1 | s2)

s1 = {1, 4, 5, 6, 2}
s2 = {5, 4, 9, 12, 11}

print(f"Union of 2 sets : {union(s1, s2)}")