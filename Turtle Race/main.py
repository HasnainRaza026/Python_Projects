from bet_winner import BetWinner
from race import Race


def main():
    bet_winner = BetWinner()
    betted_winner = bet_winner.bet_color
    race = Race()
    winner = race.start_race()

    if betted_winner in winner:
        print(f"You win, {betted_winner} turtle is the winner of the race")
    else:
        print(f"You lose, {winner[0]} turtle is the winner of the race")


if __name__ == '__main__':
    main()
