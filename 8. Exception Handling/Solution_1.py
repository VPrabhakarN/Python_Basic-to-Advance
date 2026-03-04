# Question : Write a program to handle division by zero error.

# Taking values from the user 
num1 = int(input("Enter the 1st number : "))
num2 = int(input("Enter the 2nd number : "))

try :
    div = num1 // num2
    print(f"Division : {div}")

except Exception as error :
    print(f"Something went wrong!! Error encountered : {error}")
    
