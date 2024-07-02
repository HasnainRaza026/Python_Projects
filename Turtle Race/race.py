from turtle import Turtle, Screen
import random


class Race:
    """
    A class to handle the turtle race.
    """

    def __init__(self):
        """
        Initializes the Race class and sets up the screen and turtles.
        """
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.create_turtles()

    def create_turtles(self):
        """
        Creates and positions the turtles on the screen.
        """
        colors = ['red', 'green', 'blue', 'brown', 'purple', 'pink']
        random.shuffle(colors)

        self.turtles = []
        start_y = -125
        spacing = 50

        for color in colors:
            new_turtle = Turtle()
            new_turtle.shape('turtle')
            new_turtle.color(color)
            new_turtle.penup()
            new_turtle.setpos(-285, start_y)
            start_y += spacing
            self.turtles.append(new_turtle)

    def start_race(self):
        """
        Starts the turtle race and determines the winner.

        Returns:
            str: The color of the winning turtle.
        """
        while True:
            for turtle in self.turtles:
                if turtle.xcor() >= 280:
                    return turtle.color()[0]  # Return the winning color
            random_turtle = random.choice(self.turtles)
            random_turtle.speed(random.choice([0, 10, 6, 3, 1]))
            random_turtle.fd(10)
