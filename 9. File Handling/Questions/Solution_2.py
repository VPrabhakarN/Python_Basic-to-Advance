# Question : Read a file and print how many lines it contains?

# 1st Way 
with open("9. File Handling\Questions\story.txt", "r") as file :
    lines = file.readlines()
    
    print(f"Lines : {len(lines)}")

# 2nd Way
with open("9. File Handling\Questions\story.txt", "r") as file :
    count = 0
    for line in file :
        count += 1
        
    print(f"Lines : {count}")
    

# 3rd Way 
with open("9. File Handling\Questions\story.txt", "r") as file :
    print(f"Lines : {sum(1 for line in file)}")