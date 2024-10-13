import random

# Welcome the user to the game
print("Welcome to rock, paper, scissors. Good luck!")

## Do not change this section. Please use it as it is
# Make a choice for the computer player
random_value = random.randint(1,3)
if random_value == 1:
  computer_choice = "Rock"
elif random_value == 2:
  computer_choice = "Paper"
elif random_value == 3:
  computer_choice = "Scissors"
else:
  print("Something went wrong with RANDOM")
## Your changes start below this comment

# Write your solution here, using the comments as a guide

# Get a choice from the user
# Compare the user and computer choice
# Print the right message, based on the choices
