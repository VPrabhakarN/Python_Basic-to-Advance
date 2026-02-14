# Function to count the sum of n natural numbers
def SumOfNatural(n):
    sum = 0
    
    # Using for loop 
    for i in range(1, n+1) :
        sum += i
    
    # Displaying the sum of n natural numbers
    print(f"Sum of Natural Numbers up to {n} : {sum}")  

# Taking an input from the user 
num = int(input("Enter the number : "))

# Calling the function to count the sum of n natural numbers
SumOfNatural(num)