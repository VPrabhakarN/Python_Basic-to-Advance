# Question : Remove duplicates from a list using sets.

def remove_dup(li) :
    st = set(li) 
    
    st = list(st)    
    return st

li = [10, 9, 8, 6, 6, 8, 9, 3, 1]

print(f"List after removing duplicates : {remove_dup(li)}")