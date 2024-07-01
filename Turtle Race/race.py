from turtle import Turtle, Screen
import random


class Race:
    def __init__(self):
        # Create a screen
        self.screen = Screen()
        self.screen.setup(width=600, height=600)

        self.add_turtles()

    def add_turtles(self):
        # List of colors to shuffle
        colors = ['red', 'green', 'blue', 'brown', 'purple', 'pink']
        random.shuffle(colors)

        # Create six turtles
        self.turtles = []
        start_y = -125  # Starting y-position for the first turtle
        spacing = 50  # Spacing between turtles

        for color in colors:
            self.new_turtle = Turtle()
            self.new_turtle.shape('turtle')
            self.new_turtle.color(color)
            self.new_turtle.penup()  # Lift the pen to avoid drawing lines
            self.new_turtle.setpos(-285, start_y)
            start_y += spacing
            self.turtles.append(self.new_turtle)

    def start_race(self):
        while True:
            for i in self.turtles:
                if i.xcor() >= 280:
                    return i.color()
            tur = random.choice(self.turtles)
            tur.speed(random.choice([0, 10, 6, 3, 1]))
            tur.fd(10)


if __name__ == "__main__":
    race = Race()
    race.start_race()
