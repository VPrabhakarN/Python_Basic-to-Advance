# Function 
def EvenOrOdd(num) :
    if num%2 != 0:
        return "Odd"
    else : 
        return "Even"

# Taking the input from the user 
num = int(input("Enter the number : "))

# Calling function to check the number is even or odd
print(EvenOrOdd(num))