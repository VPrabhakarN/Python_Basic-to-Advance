# Function to reverse the number 
def ReverseNumber(n) :
    sign = -1 if n < 0 else 1
    num = abs(n)
    re-verse = 0
    
    # Using while loop 
    while num > 0 :
        digit = num % 10
        reverse = (reverse*10) + digit
        num //= 10
        
    return sign*reverse

# Taking the input from the user
num = int(input("Enter a number : "))

# Calling the function to reverse the number
result = ReverseNumber(num)

# Displaying the result 
print(result)