# Question : Find first non-repeating character in string.

def first_char (text) :
    dict = {}
    
    for i in text :
        if i in dict :
            dict[i] += 1
        else :
            dict[i] = 1
            
    for key in dict :
        if dict[key] == 1 :
            return key
            
# Defining a text 
text = "thequicktfoxjumpsoverthelazydog"

# Printing first non repeating char
print(f"First Non Repeating Char : {first_char(text)}")