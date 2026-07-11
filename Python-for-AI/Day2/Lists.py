#lists

names = [ "apple", "banana", "orange","tomoto","cherry"]
# print(fruit[-1]) 

#example
import random
nums_items = len(names)
random_choice = random.randint(0, nums_items-1)
p= names[random_choice]
print(p+ "is going to buy")

# combine
names = [ "apple", "banana", "orange","tomoto","cherry"]
nam = [ "apple", "banana", "orange","tomoto","cherry"]

com = [nam, names]
print(com)

