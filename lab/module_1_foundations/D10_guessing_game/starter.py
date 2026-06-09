# D10 — Number Guessing Game
#
# Read the full brief in problem.md.
# Implement play_game() below. Run the file to play.

SECRET = 42
# On Day 29 you'll learn `random` to make the computer pick this for you.


def play_game():
    # 1. Start a guess counter at 0 (e.g. tries = 0) BEFORE the loop.
    # 2. Loop forever with `while True:`. On each pass:
    #    a. Ask for a guess with input("Guess the number (1-100): ")
    #       and convert it to an int.
    #    b. Add 1 to your guess counter.
    #    c. If the guess is greater than SECRET, print "Too high!"
    #    d. elif the guess is less than SECRET, print "Too low!"
    #    e. else (it's correct): print f"Correct! You got it in {tries} tries."
    #       and use `break` to leave the loop.
    pass


if __name__ == "__main__":
    play_game()
