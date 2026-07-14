#inheritance
# class animal:
#     def sound(self):
#         print("animal makes sound")

# class dog(animal):
#     pass
   
#     def bark(self):
#         print("can barak")

# dog1 = dog()
# dog1.bark()
# dog1.sound()


# dog2 = animal()
# dog2.sound()
# dog2.bark()  #can not access

#poly

class dog:

    def sound(self):
        print("bark")


class cat:

    def sound(self):
        print("meow")

dog1 = dog()
dog1.sound()

cat1 = cat()
cat1.sound()