class Student:
    name="karan"
    rollno="22"
    year="4th"

    def start():
        print("function used inside the class")

obj1 = Student()

#example
#create class student that takes 3 marks and has a method avg()

class Student:
         # Constructor: called automatically when an object is created
    def __init__(self, name, listOfMarks):
        self.name=name
        self.listOfMarks= listOfMarks
     
        # Method to calculate the average marks
    def avg(self):
        sum=0
         # Loop through each mark in the list
        for each in self.listOfMarks:
            sum +=each

        avg = sum/3
        print("the avg is:",avg)    

student1= Student("karan", [90,98,96])
student1.avg()
student2= Student("vihan", [60,18,76])
student2.avg()