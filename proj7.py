#ROCK PAPER SCISSOR GAME! (no UI)

import random

computer_score = 0
player_score = 0

Choices = ["rock", "paper", "scissor"]

print("Welcome to the Rock Paper Scissor Game!")
print(f"Computer Score: {computer_score} | Player Score: {player_score}")


while(computer_score < 5 and player_score < 5):
    computer_choice = random.choice(Choices)
    player_choices = input("Enter your choice (rock/paper/scissor): ").lower()
    if player_choices == computer_choice:
        print(f"Computer choice: {computer_choice}")
        print(f"Player choice: {player_choices}")
        print("It's a tie!")
    elif (player_choices == "rock" and computer_choice == "scissor") or (player_choices == "paper" and computer_choice == "rock") or (player_choices == "scissor" and computer_choice == "paper"):
        print(f"Computer choice: {computer_choice}")
        print(f"Player choice: {player_choices}")
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round!")
        print(f"Player choice: {player_choices}")
        print(f"Computer choice: {computer_choice}")
        computer_score += 1
    print(f"Computer Score: {computer_score} | Player Score: {player_score}")
if computer_score == 5:
    print("Computer wins the game! Better luck next time.")
else:
    print("Congratulations! You win the game!")
