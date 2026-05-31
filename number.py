import random

def choose_difficulty():
    """Let the player choose a difficulty level."""
    print("\nChoose Difficulty:")
    print("1. Easy (10 tries)")
    print("2. Medium (7 tries)")
    print("3. Hard (5 tries)")

    while True:
        choice = input("Enter choice (1/2/3): ")

        if choice == "1":
            return "Easy", 10
        elif choice == "2":
            return "Medium", 7
        elif choice == "3":
            return "Hard", 5
        else:
            print(" Invalid choice. Please select 1, 2, or 3.")


def generate_secret(low=1, high=100):
    """Generate a random secret number."""
    return random.randint(low, high)


def get_guess():
    """Prompt the user and return a valid integer guess."""
    while True:
        try:
            guess = int(input("Your guess (1-100): "))

            if 1 <= guess <= 100:
                return guess
            else:
                print(" Enter a number between 1 and 100.")

        except ValueError:
            print(" Numbers only, please!")


def check_guess(secret, guess):
    """Return hint string based on the guess."""
    if guess < secret:
        return "Too LOW! Guess higher."
    elif guess > secret:
        return "Too HIGH! Guess lower."
    else:
        return "CORRECT!"


def play_game():
    """Run one round of the game."""
    difficulty, max_tries = choose_difficulty()

    secret = generate_secret()

    print("\n" + "=" * 40)
    print(" PYTHON NUMBER GUESSING GAME")
    print(f" Difficulty: {difficulty}")
    print(f" Guess the number (1-100) in {max_tries} tries!")
    print("=" * 40)

    for attempt in range(1, max_tries + 1):

        print(f"\nAttempt {attempt}/{max_tries}")

        guess = get_guess()

        result = check_guess(secret, guess)

        print(f" {result}")

        if guess == secret:
            print(f" You won in {attempt} attempts!")
            return True

    print(f"\n Out of tries. The number was {secret}.")
    return False



wins = 0

while True:

    if play_game():
        wins += 1

    print(f"\n Total Wins: {wins}")

    again = input("\nPlay again? (yes/no): ").lower()

    if again != "yes":
        print("\n Thanks for playing!")
        break