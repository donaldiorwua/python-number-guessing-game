import random

def Guessing_game(guess, number):
    if guess < number:
        return "Too low! Try again."
    elif guess > number:
        return "Too high! Try again."
    else:
        return "Congratulations! You've guessed the number."
