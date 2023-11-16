'''
Alarm Clock
'''

from playsound import playsound
import time

# ANSI Escape codes to clear the terminal and return courser to home position
clear = "\033[2J"
clear_and_return = "\033[2H"

def alarm (seconds):
    time_elapsed = 0

    # Clears the terminal
    print(clear)

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        # Clears and return the courser to the home position after each itteration 
        print(f"{clear_and_return}Alarm will ring in::  {minutes_left:02d} mim : {seconds_left:02d} sec")

    playsound("Alarm.wav")


minutes = int(input("Enter number of minutes: "))
seconds = int(input("Enter number of seconds: "))

total_seconds = seconds +  minutes*60 
alarm(total_seconds)