# Question : Count frequency of characters in a string.

def count_frq(text) :
    dict = {}
    
    for i in text :
        if i in dict :
            dict[i] += 1
        else :
            dict[i] = 1
            
    return dict

# Defining string
text = "My name is vijay"

# Counting the freqency of characters in a string
print(f"Count of Freqency : {count_frq(text)}")