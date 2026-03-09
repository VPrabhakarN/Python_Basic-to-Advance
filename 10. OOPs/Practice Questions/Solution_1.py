# Question :Create a class that takes name & marks of 3 subjects as an arguments in contructor. Then create a nethod to print the average of the marks.

class Student :
    
    # Defining constructor to initialise the memory
    def __init__(self, name, marks) :
        self.name = name
        self.marks = marks
        
    # Defining the method to print the average of the marks along with the student details 
    def average_marks(self) :
        # count = 0
        # sum = 0
        # for item in self.marks :
        #     count += 1
        #     sum += item
        result = sum(self.marks)/len(self.marks)
            
        print(f"Name : {self.name}")
        print(f"Average marks : {result}")
         
# Creating an object
S1 = Student("Vijay", [93, 95, 99])

# Displaying the name and average marks
S1.average_marks()