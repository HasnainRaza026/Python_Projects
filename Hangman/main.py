import re
from os import system, name
import random
import time
from hangman_art import *
from hangman_words import *


def find_position(text, word):
    pattern = r'\b' + re.escape(word) + r'\b'
    matches = re.finditer(pattern, text, re.IGNORECASE)
    positions = [match.start() for match in matches]
    return positions

def clear_terminal():
      # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


print(logo)

time.sleep(0.5)
clear_terminal

word = random.choice(word_list)
print(word)

print(f"Your word is a {len(word)} letter word")

guess = "_ " * len(word)
count = 1
display_stage = stages[len(stages)-count]

while True:
    print(guess)
    print(display_stage)
    letter = input("Choose a letter: ")
    quantity = word.count(letter)
    if "_" not in guess or display_stage==stages[0]:
        print(f"You loose")
        break
    elif quantity != 0:
        position = find_position(word, letter)
        for i in position:
            new_guess = guess[:i + 1] + letter + guess[i + 2:]
            guess = new_guess
    elif quantity == 0:
        print(f"You guessed {letter}, that is not in the word. You lose a life")
        count += 1
        display_stage = stages[len(stages)-count]
    clear_terminal


    