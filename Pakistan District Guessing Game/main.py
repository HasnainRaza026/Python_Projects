import time
from turtle import Screen
from display_district import DisplayDistrict
import pandas as pd


def main():
    screen = Screen()
    screen.setup(width=800, height=556)
    screen.bgpic('districts_of_pakistan_map.gif')
    screen.tracer(0)

    district_data = pd.read_csv('district.csv')
    guessed_districts = []
    score = 0
    total_districts = len(district_data)

    while len(guessed_districts) < total_districts:
        district_name = screen.textinput(
            f'Score: {score}/{total_districts}', 'Enter District name:').strip().title()
        if district_name in guessed_districts:
            print(f"You've already guessed {district_name}")
        elif district_name in district_data['Districts'].values:
            district_index = district_data.index[district_data['Districts'] == district_name].tolist(
            )
            x = district_data.at[district_index[0], 'X']
            y = district_data.at[district_index[0], 'Y']
            display_district = DisplayDistrict(x, y, district_name)
            guessed_districts.append(district_name)
            score += 1
            print(f"Correct! {district_name} is on the map.")
        else:
            print(f"{district_name} does not exist")

        screen.update()
        time.sleep(0.1)

    print(f"Game Over! Your final score is {score}/{total_districts}")
    play_again = screen.textinput(
        "Game Over", "Do you want to play again? (yes/no)").strip().lower()
    if play_again == "yes":
        screen.clearscreen()
        main()
    else:
        screen.bye()


if __name__ == "__main__":
    main()
