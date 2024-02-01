import random

hangman1 = [
"""
+---+
    |
    |
    |
    ===""", """
+---+
  | |
  0 |
    |
    ===""", """
+---+
  | |
  0 |
 /  |
    ===""", """
+---+
  | |
  0 |
 / \|
    ===""", """
+---+
  | |
  0 |
 / \|
  | ===""", """
 /
+---+
  | |
  0 |
 / \|
  | ===""", """
 / \ 
       """
]

animals = ['tiger','lion','dolphin','dog','cow','shark','giraffe','elephant','crow']

word = random.choice(animals).lower()

guessed_correctly = []
guessed_incorrectly = []
tries = 6
hangman_count = -1
while tries > 0:
    output =''
    for letter in word:
        if letter in guessed_correctly:
            output += letter
        else:
            output += '_ ' 
    if output == word:
        break

    print("guess the word: ", output)
    print(tries, " chances left") 
    guess = input().lower()
    if guess in guessed_correctly or guess in guessed_incorrectly:
        print("Already guessed",guess)
    elif guess in word:
        print("nice job!! You guessed a correct word congrates!")
    else:
        print("Sorry dear! You guessed a wrong word try again!")
        hangman_count = hangman_count + 1
        tries = tries - 1
        guessed_incorrectly.append(guess)
        print(hangman1[hangman_count])

if tries > 0:
    print("WOW You guess the word correctly and you win!!!")
else:
    print("Sorry guessed a wrong word. Try again")
    
