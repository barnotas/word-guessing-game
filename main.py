"""
File: word_guess.py
-------------------
Fill in this comment.
"""

import random

LEXICON_FILE = "Lexicon.txt"  # File to read word list from
INITIAL_GUESSES = 8  # Initial number of guesses player starts with


def play_game(secret_word):
    k = 8
    dash = ' '
    for i in range(len(secret_word)):
        dash = dash + "-"

    while k != 0 and dash.find("-") != -1:
        print("The word now looks like this:", dash)
        print("You have", k, "guesses left ")
        guess = input("Type a single letter here, then press enter: ")

        if len(guess) != 1:
            print("Guess should only be a single character.")
            print("The word now looks like this:", dash)
            print("You have", k, "guesses left")
            guess = input("Type a single letter here, then press enter: ").upper()
        if secret_word.find(guess) != -1:
            print("That guess is correct.")

            for i in range(len(secret_word)):
                if guess == secret_word[i]:
                    dash = dash[:i] + guess + dash[i + 1:]

        elif guess not in secret_word:

            print("There are no " + str(guess) + "'s in the word")
            k -= 1

        if "-" not in dash:
            print("Congratulations, the word is:", secret_word)


def get_word():
    with open(LEXICON_FILE) as file:
        text = file.read()
        secret_word = list(map(str, text.split()))
    return random.choice(secret_word)


def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
