# Question : Take user input and handle invalid integer input.

try :
    # Taking an input from the user
   num = int(input("Enter the number : "))
   print(f"The number you enetred : {num}")
   
except Exception as error :
    print(f"Error Occupied : {error}")
    
    