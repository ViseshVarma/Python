""" Number Guessing Game """

import random
print("Welcome to the Number Guessing game!")

Easy = 10
Hard = 5
# Function to check the user's guess against actual answer.
def check_answer(target, guess):
    if(guess > target):
        print("Too Low")
    elif(guess < target):
        print("Too High")
    else:
        print(f"You got it! The answer was {target}")
        
# Create a function to set difficulty
def difficulty():
    difficulty = input("Choose a Difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return Easy
    else:
        return Hard
    
turns = difficulty()
print(f"You have {turns} attempts remaining to guess the number.")

# step 1 : choose a random number between 1 and 100
print("I'm thinking of a number between 1 and 100.")
target = random.randint(1, 100)

# Repeat the guessing functionality if they get it wrong.
guess = 0
while guess != target and turns > 0:
    # Let the user guess a number
    guess = int(input("Make a guess: "))
    turns = turns - 1
    # Track the number of attempts remaining.
    print(f"You have {turns} attempts remaining to guess the number.")
    
    check_answer(guess, target)



