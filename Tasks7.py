#hangman game

import random

# Predefined word list
words = ["python", "guitar", "science", "elephant", "football"]
word = random.choice(words)  # Player 1 selects a random word
hidden_word = ["_"] * len(word)
attempts, max_attempts = 0, 6  # Max 6 incorrect guesses (hangman stages)
guessed_letters = set()

print("Welcome to AI Hangman!\n")

while attempts < max_attempts:
    print("Word:", " ".join(hidden_word))
    guess = input("Player 2, guess a letter: ").lower()

    if guess in guessed_letters:
        print("Already guessed! Try another letter.")
        continue

    guessed_letters.add(guess)

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                hidden_word[i] = guess
        print("Correct guess!")
    else:
        attempts += 1
        print(f"Wrong guess! {max_attempts - attempts} attempts left.")

    if "_" not in hidden_word:
        print("🎉 Player 2 wins! The word was:", word)
        break
else:
    print("💀 Player 1 wins! The word was:", word)
