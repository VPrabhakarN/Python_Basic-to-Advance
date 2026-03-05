# Question : Write a program to count total words in a file.

# 1st Way 
with open(r"9. File Handling\Questions\story.txt", "r") as file :
    data = file.read()
    words = data.split()
    print(f"Words : {len(words)}")