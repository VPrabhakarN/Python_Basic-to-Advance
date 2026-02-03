# Question : Greet by gender -> Accept gender input ('m' or 'f') and print greeting accordingly

# Taking the input from the user
gender = input("Enter your gender (M/F) : ")

# Usinf elif statement to check the conditions 
if gender == 'M' or gender == 'm' :
    print("Hello Ma'am, Good Morning!")
elif gender == 'F' or 'f' :
    print("Hello Sir, Good Morning !")
else:
    print("Invalid Input !!! Please enter valid gender !!")

    
