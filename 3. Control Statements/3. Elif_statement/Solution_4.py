# Question : Voting Eligibility -> Input name and age, If age >= 18, print "Eligible to vote", If not, print how many years are left to become eligible.

# Taking input from the user 
name = input("Enter your name : ")
age = int(input("Enter your age : "))

# Using elif statement to check the conditions 
if age >= 18 :
    print("Hello " + name + ", You are Eligible to vote !")
elif age < 18 :
    years_left = 18 - age 
    print("Hello " + name + ", You are not Eligible to vote yet. Hopefully, you will be eligible to vote in " + str(years_left) + " years.")