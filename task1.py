
import random

# List of 5 predefined words
words = ["python", "computer", "coding", "developer", "program"]

# Select a random word
secret_word = random.choice(words)

# Game variables
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("================================")
print("       HANGMAN GAME")
print("================================")
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses allowed.")

# Main game loop
while incorrect_guesses < max_attempts:

    # Display the word with hidden letters
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses left:", max_attempts - incorrect_guesses)

    # Check whether the player has won
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You guessed the word:", secret_word)
        break

    # Take input from the player
    guess = input("Enter a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    # Check repeated guesses
    if guess in guessed_letters:
        print("You have already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check the guessed letter
    if guess in secret_word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

# Check whether the player lost
if incorrect_guesses == max_attempts:
    print("\nGame Over!")
    print("The correct word was:", secret_word)

print("\nThanks for playing Hangman!")
