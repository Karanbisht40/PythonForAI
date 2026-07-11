#rock, paper, scissors game
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