# Function : 
def number_check(num) :
    # Using if-elif-else statement
    if num > 0 :
        return "Positive"
    elif num < 0 :
        return "Negative"
    else :
        return "Zero"
    
# Taking the value from the user 
num = int(input("Enter the number : "))

# Calling the function to check whether the number is positive, negative or zero
print(number_check(num))