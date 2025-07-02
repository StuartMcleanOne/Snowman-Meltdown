import random
from statistics import StatisticsError

# List of secret words

WORDS = ["python", "git", "github", "snowman", "meltdown"]

# Snowman ASCII Art Stages

STAGES = [
     # Stage 0: Full snowman
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
     # Stage 1: Bottom part starts melting
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
     # Stage 2: Only the head remains
     """
      ___  
     /___\\ 
     (o o) 
     """,
     # Stage 3: Snowman completely melted
     """
      ___  
     /___\\ 
     """
 ]

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

    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)

    mistakes = 0

    guessed_letters = [] #a list to store all the guessed letters

    display_game_state(mistakes, secret_word, guessed_letters) #Visual and word rendering

    guess = input("Guess a letter: ").lower()
    guessed_letters.append(guess) # Adds players guess to the list of guessed letters.
    print("You guessed:", guess)

if __name__ == "__main__":
    play_game()
