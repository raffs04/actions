
import random

def guessing_game():
    print("Welcome to the Guessing Game!")

    secret_number = random.randint(1, 100)

    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            guess = int(input("Guess the number (between 1 and 100): "))
            attempts += 1

            if guess == secret_number:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

        except ValueError:
            print("Please enter a valid number.")

    else:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

guessing_game()