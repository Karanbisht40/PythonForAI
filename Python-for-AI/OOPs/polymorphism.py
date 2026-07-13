#Polymorphism means one interface, many forms.
#  The same method name can behave differently depending on the object.

class Dog:

    def sound(self):
        print("Bark")

class Cat:

    def sound(self):
        print("Meow")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()