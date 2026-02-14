# function to count number of digit 
def CountDigit(n) :
    copy = n
    # Making it absolute 
    n = abs(n)
    count = 0
    
    # Using if-else condition 
    if num != 0 :
        # Using while loop
        while n > 0 :
            digit = n%10
            count += 1
            n //= 10
    else :
        count += 1
    
    # Displaying the count of numbers 
    print(f"Count of numbers in {copy} is {count}.")        

# Taking an input from 
num = int(input("Enter a number : "))

# Calling a function to count number of digit
CountDigit(num) 