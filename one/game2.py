import random

def guessing_game(user_input_func=input):
    print("Welcome to the Guessing Game!")

    secret_number = random.randint(1, 100)

    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            guess = int(user_input_func("Guess the number (between 1 and 100): "))
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

# Call the function without input parameter to use standard input
#guessing_game()

def test_guessing_game():
    # Example test where user always inputs 42
    user_inputs = ["42"] * 10
    user_input_iter = iter(user_inputs)
    guessing_game(lambda _: next(user_input_iter))

# Run the test
test_guessing_game()


