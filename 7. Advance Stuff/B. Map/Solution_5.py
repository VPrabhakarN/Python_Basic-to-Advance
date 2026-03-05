# Question : Convert a list of temperatures from Celsius to Fahrenheit.

# Defining a list 
celsius = [32, 33, 34, 35, 36, 37]

# Converting temperatures from celsius to fahrenheit 
result = map(lambda x:(x*1.8+32), celsius)

# Displaying the temperatures in fahrenheit 
print(f"Temperatures in Fahrenheit : {list(result)}")