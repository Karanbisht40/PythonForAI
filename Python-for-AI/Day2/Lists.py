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


import random

choices = ["Rock", "Paper", "Scissors"]

player = random.randint(0, 2)
computer = random.randint(0, 2)

print("Player:", choices[player])
print("Computer:", choices[computer])

# 0 = rock, 1 =paper, 2 =sissors
if player == computer:
    print("Draw")
elif (player == 0 and computer == 2) or \
     (player == 1 and computer == 0) or \
     (player == 2 and computer == 1):
    print("Player Wins")
else:
    print("Computer Wins")