# Function
def Mul_Table(n) :
    # Using the for loop to print the table
    for i in range(1, 11) :
        print(f"{n} X {i} = {n*i}")

# Taking the input from the user
num = int(input("Enter the number : "))

# Calling the function to print the table
Mul_Table(num)
