# Write a python program to build a random number guess game

import random

user_score = 0
computer_score = 0

# Using while loop 
while True :
    #Current Scores
    print(f"Current scores -> Your Score :- {user_score} | Computer Score :- {computer_score}")
    
    # Taking the number from the user 
    user_num = int(input("1 for stone, 2 for paper, 3 for scissor : ")) 
    computer_num = random.randint(1,3) 


    # Using if-elif-else statement 
    if user_num == 1 and computer_num == 3:
        print("Congratulations!! You won !!\n")
        user_score += 1
        
    elif user_num == 2 and computer_num == 1 :
        print("Congratulations!! You won !!\n")
        user_score += 1
        
    elif user_num == 3 and computer_num == 2:
        print("Congratulations!! You won !!\n")
        user_score += 1
        
    elif user_num == computer_num :
        print("It's Draw!!\n")
        
    else :
        print("Computer Won !! You Lost !!!\n")
        computer_score += 1
        
    if user_score == 5 :
        print("You Nailed it!! You won the game!!\n")
        break
    elif computer_score == 5 :
        print("You Lost the GAME !! Computer won the game!!\n")
        break
        




