import random
import sys
import subprocess

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]


def deal_card():
    """Returns a random card from the deck."""
    return random.choice(CARDS)


def calculate_score(cards):
    """Calculates the score of the current hand."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def hit(cards):
    """Draws a card and adds to the current hand."""
    cards.append(deal_card())
    return cards


def display_scores(user, computer):
    """Displays the current scores of both user and computer."""
    print(f"Your cards: {user}, current score: {calculate_score(user)}")
    print(f"Computer's first card: {computer[0]}")


def clear_terminal():
    """Clears the terminal screen."""
    operating_system = sys.platform
    if operating_system == 'win32':
        subprocess.run('cls', shell=True)
    else:
        subprocess.run('clear', shell=True)


def start():
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
        play_game()
    print("Thanks for playing!")


def play_game():
    clear_terminal()
    print(logo)

    user = [deal_card(), deal_card()]
    computer = [deal_card()]

    display_scores(user, computer)

    game_over = False
    while not game_over:
        if calculate_score(user) == 0 or calculate_score(user) > 21:
            game_over = True
        else:
            if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
                user = hit(user)
                display_scores(user, computer)
            else:
                game_over = True

    while calculate_score(computer) != 0 and calculate_score(computer) < 17:
        computer = hit(computer)

    display_final_scores(user, computer)


def display_final_scores(user, computer):
    user_score = calculate_score(user)
    computer_score = calculate_score(computer)

    print(f"Your final hand: {user}, final score: {user_score}")
    print(f"Computer's final hand: {computer}, final score: {computer_score}")

    if user_score == computer_score:
        print("It's a draw!")
    elif user_score == 0:
        print("You have a Blackjack! You win!")
    elif computer_score == 0:
        print("Computer has a Blackjack! You lose!")
    elif user_score > 21:
        print("You went over. You lose!")
    elif computer_score > 21 or user_score > computer_score:
        print("You win!")
    else:
        print("You lose!")


if __name__ == "__main__":
    start()
