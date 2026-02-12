# Write a python program to build a random number guess game

import random

# Generate a random number between 1 and 100
num = random.randint(1, 100)

# Initialize number of tries
tries = 0

# Using while loop
while True:
    
    # Increase try count
    tries += 1

    # Taking input from the user
    guessed = int(input("Enter the number: "))

    # If-elif condition
    if guessed == num:
        print(f"Congratulations!! You entered the correct number in {tries} tries.")
        break

    elif guessed > num:
        print("Sorry, you need to go a little lower!\n")

    elif guessed < num:
        print("Sorry, you need to go a little higher!\n")
