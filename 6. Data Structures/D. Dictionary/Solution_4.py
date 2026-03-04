# Question : Create a dictionary from two lists (keys & values).

def creat_dict (num1, num2) :
    dict = {}
    
    for i in range(len(num1)) :
        dict[num1[i]] = num2[i]
            
    return dict

# Defining two lists
num1 = [1, 2, 3, 4, 5]
num2 = [6, 7, 8, 9, 10]

# Creating dictionary using two lists
print(f"Dictionary : {creat_dict(num1, num2)}")