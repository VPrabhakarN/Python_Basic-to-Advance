# Program to open the file and then close the file 
file = open("9. File Handling\File_Close.py", "r")

# Printing the file details
print(f"File Name : {file.name}")
print(f"File Mode : {file.mode}")
print(f"File Closed : {file.closed}")

# Closing the file 
file.close()

print(f"File Closed : {file.closed}")