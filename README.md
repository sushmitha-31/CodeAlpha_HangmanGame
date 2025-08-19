# Hangman Game 🎯

A simple text-based Hangman game built in Python for the *CodeAlpha Internship*.

## Features
- 5 predefined words.
- 6 wrong guesses allowed.
- Console-based input and output only.
- Uses random, while, if-else, strings, and lists.

## How to Run
1. Make sure you have *Python 3* installed.
2. Download or clone this folder.
3. Open a terminal in this folder and run:
   ```bash
   python hangman.py
4.Follow the onscreen instructions.

**Example Winning Output**
🎯 Welcome to Hangman Game!

     +---+
     |   |
         |
         |
         |
         |
    =========

_ _ _ _ _ _ _

Enter a letter: p
✅ Good guess!

     +---+
     |   |
         |
         |
         |
         |
    =========
    
_ _ _ p _ _ _

Enter a letter: c
✅ Good guess!

     +---+
     |   |
         |
         |
         |
         |
    =========
    
c _ _ p _ _ _

Enter a letter: y
✅ Good guess!

     +---+
     |   |
         |
         |
         |
         |
    =========

c _ _ p _ _ y

Enter a letter: m
✅ Good guess!

     +---+
     |   |
         |
         |
         |
         |
    =========

c _ m p _ _ y

Enter a letter: n
✅ Good guess!

     +---+
     |   |
         |
         |
         |
         |
    =========

c _ m p _ n y

Enter a letter: o
✅ Good guess!

     +---+
     |   |
         |
         |
         |
         |
    =========

c o m p _ n y

Enter a letter: a
✅ Good guess!

     +---+
     |   |
         |
         |
         |
         |
    =========

c o m p a n y
🎉 Congratulations! You guessed the word.


**Example Losing Output**
🎯 Welcome to Hangman Game!

     +---+
     |   |
         |
         |
         |
         |
    =========

_ _ _ _ _ _ _ _ _ _

Enter a letter: p
✅ Good guess!

     +---+
     |   |
         |
         |
         |
         |
    =========
    
_ _ _ _ _ _ _ _ _ p

Enter a letter: y
❌ Wrong guess! Attempts left: 5

     +---+
     |   |
     O   |
         |
         |
         |
    =========

_ _ _ _ _ _ _ _ _ p

Enter a letter: z
❌ Wrong guess! Attempts left: 4

     +---+
     |   |
     O   |
     |   |
         |
         |
    =========

_ _ _ _ _ _ _ _ _ p

Enter a letter: y
⏳You already guessed that letter.

Enter a letter: x
❌ Wrong guess! Attempts left: 3

     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========

_ _ _ _ _ _ _ _ _ p

Enter a letter: b
❌ Wrong guess! Attempts left: 2

     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========

_ _ _ _ _ _ _ _ _ p

Enter a letter: f
❌ Wrong guess! Attempts left: 1

     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========

_ _ _ _ _ _ _ _ _ p

Enter a letter: g
❌ Wrong guess! Attempts left: 0

     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========

_ _ _ _ _ _ _ _ _ p
💀 Game Over! The word was 'internship'.


---

## 👩‍💻 Author  
*Sushmitha M S*

## 🏢 Internship  
*CodeAlpha – Python Programming*
