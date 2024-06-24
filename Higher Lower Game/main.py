import random
import sys
import subprocess
from art import *
from game_data import data

def clear_terminal():
    operating_system = sys.platform
    if operating_system == 'win32':
        subprocess.run('cls', shell=True)
    else:
        subprocess.run('clear', shell=True)

def get_new_choice(exclude_choice):
    """Select a new random choice different from the excluded one."""
    new_choice = random.choice(data)
    while new_choice == exclude_choice:
        new_choice = random.choice(data)
    return new_choice

def initial_pick():
    """Select the initial two random choices."""
    first = random.choice(data)
    second = random.choice(data)
    while first == second:
        second = random.choice(data)
    return first, second

def main():
    current, next_choice = initial_pick()
    score = 0
    lost = False

    print(logo)

    while not lost:
        print(f"Compare A: {current['name']}, a {current['description']}, from {current['country']}")
        print(vs)
        print(f"Compare B: {next_choice['name']}, a {next_choice['description']}, from {next_choice['country']}")

        ans = input("Who has more followers? Type 'A' or 'B': ").lower()

        if (ans == "a" and current['follower_count'] > next_choice['follower_count']) or \
           (ans == "b" and current['follower_count'] < next_choice['follower_count']):
            score += 1
            clear_terminal()
            print(f"You are right! Current score: {score}")
            if ans == "a":
                current = next_choice
                next_choice = get_new_choice(current)
            else:
                next_choice = get_new_choice(current)
        else:
            print(f"Sorry, that was wrong. Final score: {score}")
            lost = True

if __name__ == "__main__":
    main()
