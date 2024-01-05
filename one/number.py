import random


def guessing_game():
    number_to_guess = random.randint(1, 100)

    while True:
        guess = int(input("Guess the number (between 1 and 100): "))

        if guess == number_to_guess:
            print("Congratulations! You guessed the correct number.")
            break
        elif guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")


if __name__ == "__main__":
    print("Welcome to the Guessing Game!")
    guessing_game()
