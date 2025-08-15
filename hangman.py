import random

words = ["codealpha", "internship", "hangman", "python", "company"]

HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

def choose_word():
    return random.choice(words)

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts_left = 6

    print("🎯 Welcome to Hangman Game!")
    print(HANGMAN_PICS[0])
    print("_ " * len(word_to_guess))

    while attempts_left > 0:
        guess = input("\nEnter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠ Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("⏳You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("✅ Good guess!")
        else:
            attempts_left -= 1
            print(f"❌ Wrong guess! Attempts left: {attempts_left}")

        print(HANGMAN_PICS[6 - attempts_left])

        display_word = ""
        for letter in word_to_guess:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(display_word.strip())

        if "_" not in display_word:
            print("🎉 Congratulations! You guessed the word.")
            break
    else:
        print(f"💀 Game Over! The word was '{word_to_guess}'.")

if __name__ == "__main__":
    hangman()
