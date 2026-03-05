# Question : Write a program to read a file story.txt and print its entire content.

# Reading file 
with open("9. File Handling\Questions\story.txt", "r") as file :
    data = file.read()
    print(data)
    
print("\n Closed the file \n")