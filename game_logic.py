import random
from ascii_art import STAGES

# List of secret words

WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """ Selects a  random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters):
    """ Displays the current snowman stage and partially guessed word."""
    print(STAGES[mistakes])# Displays snowman in current melting state based on mistake count
    display_word = "" # Sets up empty string to build word display
    for letter in secret_word: # Loops through each letter of the secret word.
        if letter in guessed_letters:
            display_word += letter + " " # If player guesses display letter else show underscore
        else:
            display_word += "_ "
    print("Word.", display_word.strip())


def play_game():
    secret_word = get_random_word()
    mistakes = 0
    guessed_letters = [] #a list to store all the guessed letters
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)

    while True:
        display_game_state(mistakes, secret_word, guessed_letters) #Visual and word rendering
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess) # Adds players guess to the list of guessed letters.

        if guess not in secret_word:
            mistakes += 1
            print("Wrong guess!")

        #Check win condition
        if all(letter in guessed_letters for letter in secret_word):
            display_game_state(mistakes, secret_word, guessed_letters)
            print("Congratulations. You win!")
            break

        if mistakes >= max_mistakes:
            display_game_state(mistakes, secret_word, guessed_letters)
            print(f"Snowman melted. Game over! The word was '{secret_word}'.")
            break





        print("You guessed:", guess)
