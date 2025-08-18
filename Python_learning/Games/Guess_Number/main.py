# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random

level = input("Write the level you want to play easy / hard : ")

## Chek the level user selected to play
if level == "easy":
    attempts = 10
elif level == "hard":
    attempts = 5
else:
    print("Please only input either easy or hard ")
    exit(0)
print("You have to guess a number between 1 and 100 ")


# call the function to generate the required random number
def random_number_generator():
    number = random.randint(1, 100)
    return number


def guess_number():
    guess_number = int(input("Enter the number to Guess: "))
    return guess_number


## Loop through the attmepts as per the level
random_number = random_number_generator()
for count in range(attempts):
    guess = guess_number()

    print(random_number, guess)
    if attempts != 0:
        if guess == random_number:
            print("You Guessed it !")
            exit(0)
        elif guess > random_number:
            print("You guessed too high")
            print("Guess again")
            attempts = attempts - 1
            print(f"You have {attempts} remaining")
        elif guess < random_number:
            print("You guessed too low")
            attempts = attempts - 1
            print(f"You have {attempts} remaining")

print("You lost all your chances")
