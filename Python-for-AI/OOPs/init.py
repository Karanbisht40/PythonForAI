class Student:
    name="karan"
    rollno="22"
    year="4th"
     #self ke sth pass kr skte h
    def __init__(self, branch, course):
       print("whenver a object is created i am called automatically")
       print(self)
       self.branch= branch
       self.course= course
   
   #obj banne skte pass kr skte h
obj1 = Student("cse", "btech")
print(obj1.branch)
print(obj1.course)

obj2 = Student("me","btech")
print(obj2.branch)
print(obj2.course)