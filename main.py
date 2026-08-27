import random
from game import Guessing_game


def main():
    print("========================================")
    print("Welcome to the Number Guessing Game!")
    print("========================================")
    print("I'm thinking of a number between 1 and 100.")

    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5
    
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
            result = Guessing_game(guess, number)
            print(result)
            if result.startswith("Congratulations"):
                break
            if not result.startswith("Congratulations"):
                print(f"You guessed the number in {attempts} attempts!, you have {max_attempts - attempts} attempts left.")
            elif attempts == max_attempts:
                print(f"You've used all {max_attempts} attempts. The number was: {number}!")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()