import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while True:
        # Prompt the user to input their guess
        guess = input("Enter your guess (1-100): ")

        # Validate the input
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Increment the number of attempts
        attempts += 1

        # Compare the guess to the secret number
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} correctly!")
            print(f"It took you {attempts} attempts to win the game.")
            break

# Run the game
number_guessing_game()