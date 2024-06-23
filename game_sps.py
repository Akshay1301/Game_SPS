"""
Combinations:
Rock & Paper --> Paper
Rock & Scissor --> Rock
Scissor & Paper --> Scissor
same --> No Winner, another try


"""

import random #Importing Random module

option = ["Stone", "Paper", "Scissor","stone", "paper", "scissor","STONE","PAPER","SCISSOR"]

computer_choice = random.choice(option)
player_choice = input("Please enter your choice (Stone/Paper/Scissor): ")
print(f"Your Choice = {player_choice}.")
print(f"Computer's Choice = {computer_choice}.")

if player_choice == "Stone" or player_choice == "stone":
    if computer_choice == "Stone" or computer_choice == "stone" or computer_choice == "STONE":        
        print("Game is tied.")
    elif computer_choice == "Paper" or computer_choice == "paper" or computer_choice == "PAPER":
        print("You have lost the Game.")
    elif computer_choice == "Scissor" or computer_choice == "SCISSOR" or computer_choice == "scissor":
        print("You have won the Game.")
elif player_choice == "Paper" or player_choice == "paper":
    if computer_choice == "Stone" or computer_choice == "stone" or computer_choice == "STONE":
        print("You have won the Game.")
    elif computer_choice == "Paper" or computer_choice == "paper" or computer_choice == "PAPER":
        print("Game is tied.")
    elif computer_choice == "Scissor" or computer_choice == "SCISSOR" or computer_choice == "scissor":
        print("You have lost the Game.")
elif player_choice == "Scissor" or player_choice == "scissor":
    if computer_choice == "Stone" or computer_choice == "stone" or computer_choice == "STONE":
        print("You have lost the Game.")
    elif computer_choice == "Paper" or computer_choice == "paper" or computer_choice == "PAPER":
        print("You have won the Game.")
    elif computer_choice == "Scissor" or computer_choice == "SCISSOR" or computer_choice == "scissor":
        print("Game is tied.")
else:
    print("Please enter appropriate option for a match")
