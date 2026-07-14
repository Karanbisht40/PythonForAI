
#Encapsulation means wrapping data (variables) and methods
#(functions) into a single unit (class) and restricting direct access to the data.
class Student:

    def __init__(self):
        self.name = "Karan"
        self.__marks = 95   # Private variable

    def show_marks(self): #accessing private variable through function
        print(self.__marks)

student = Student()

student.show_marks() 