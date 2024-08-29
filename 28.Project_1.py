""" 
ROCK PAPER SCISSOR GAME

RULES:- Rock wins against Scissors
        Scissor wins against Paper
        Paper wins against Rock
        
i.e.    if 1st user select rock and 
        2nd user select rock then user 1 wins

"""

import random

user_choice = int(input("Enter your Choice: Type 0 for Rock, 1 for Paper, 2 For Scissor."))

if user_choice > 2 or user_choice < 0:
    print("Invalid Input")
else:
    computer_choice=random.randint(0,2)

    print("Computer Chose:")

    print(computer_choice)

    if computer_choice == user_choice:
        print("It's a draw.")
    elif computer_choice == 0 and user_choice == 2:
        print("You Lose.")
    elif computer_choice == 2 and user_choice == 0:
        print("You win")
    elif computer_choice > user_choice:
        print("You lose")
    elif computer_choice < user_choice:
        print("You win.")