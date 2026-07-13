#Inheritance allows one class to inherit the properties and methods of another class.
class Animal:

    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    pass

dog = Dog()
dog.sound()