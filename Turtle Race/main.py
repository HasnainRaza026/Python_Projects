from bet_winner import BetWinner
from race import Race


def main():
    """
    The main function to run the turtle race game. 
    It handles user bets and starts the race.
    """
    bet_winner = BetWinner()
    betted_color = bet_winner.bet_color

    if betted_color is None:
        print("No bet was placed. Exiting the game.")
        return

    race = Race()
    winning_color = race.start_race()

    if betted_color == winning_color:
        print(
            f"You win! The {winning_color} turtle is the winner of the race.")
    else:
        print(
            f"You lose. The {winning_color} turtle is the winner of the race.")


if __name__ == '__main__':
    main()
