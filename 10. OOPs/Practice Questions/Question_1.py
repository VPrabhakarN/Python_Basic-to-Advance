# Question 1

# Creating a class
class Employee :
    def __init__(self, name, salary) :
        self.name = name
        self.salary = salary
        
    # Defining dunder/magic method
    def __str__ (self) :
        return f"Your name is {self.name} and your salary is {self.salary}."
        

# Creating an instance of the class
emp = Employee("Vijay", 350000)
print(emp)