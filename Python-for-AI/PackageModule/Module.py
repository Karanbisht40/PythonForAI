
#importing module from  another file
import MyModule
MyModule.hello("karan")
MyModule.bye("rohan")
MyModule.go("roman")

#access specific part of code   
from MyModule import person1 
print(person1["course"])