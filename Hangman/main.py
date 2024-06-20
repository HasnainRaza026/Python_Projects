import sys, subprocess
import random
import time
from hangman_art import *
from hangman_words import *


def find_position(text, word):
    positions = []
    start = 0
    while True:
        start = text.find(word, start)
        if start == -1:
            break
        positions.append(start)
        start += len(word)  # Move past the word
    return positions

def clear_terminal():
    operating_system = sys.platform
    if operating_system == 'win32':
        subprocess.run('cls', shell=True)
    else:
        subprocess.run( 'clear', shell=True)


print(logo)

time.sleep(1)
clear_terminal()

word = random.choice(word_list)
# print(word)

print(f"Your word is a {len(word)} letter word")

guess = "_ " * len(word)
count = 1
display_stage = stages[len(stages)-count]
print(display_stage)

while True:
    if "_" not in guess:
        print(f"You guesed the word correctly, You Won!")
        break
    print(guess)
    letter = input("Choose a letter: ")
    quantity = word.count(letter)
    if quantity != 0:
        position = find_position(word, letter)
        for i in position:
            if i == 0:
                guess = letter + guess[i+1:] 
            else:
                guess = guess[:i*2] + letter + guess[i*2+1:] 
        print(display_stage)
    elif quantity == 0:
        print(f"You guessed {letter}, that is not in the word. You lose a life")
        count += 1
        display_stage = stages[len(stages)-count]
        if display_stage==stages[0]:
            print(display_stage)
            print(f"You lost")
            break
        print(display_stage)
    


    