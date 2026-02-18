#its a number guessing game

import random

number = random.randint(1,100)
guess = 0
a = -1

while(a != number):
    guess += 1
    a = int(input("Guess the number: "))
    if(a > number):
        print("Lower number please")
    else:
        print("Higher number please")
print(f"Congratulations! You guessed the number in {guess} guesses.")