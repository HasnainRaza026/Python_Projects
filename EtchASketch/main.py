from turtle import Turtle, Screen


class TurtleController:
    """
    A class to handle turtle movements and screen interactions.
    """

    def __init__(self):
        """
        Initializes the TurtleController class, sets up the screen, and binds keys to actions.
        """
        self.turtle = Turtle()
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.turtle.speed(1)  # Set the initial speed of the turtle
        self.bind_keys()

    def bind_keys(self):
        """
        Binds keyboard keys to turtle movement functions.
        """
        self.screen.listen()
        self.screen.onkey(self.move_forward, "Up")
        self.screen.onkey(self.move_backward, "Down")
        self.screen.onkey(self.turn_left, "Left")
        self.screen.onkey(self.turn_right, "Right")
        self.screen.onkey(self.clear_screen, "c")
        self.screen.onkey(self.increase_speed, "plus")
        self.screen.onkey(self.decrease_speed, "minus")
        self.screen.onkey(self.stop_movement, "space")

    def move_forward(self):
        """
        Moves the turtle forward.
        """
        self.turtle.fd(20)

    def move_backward(self):
        """
        Moves the turtle backward.
        """
        self.turtle.bk(20)

    def turn_left(self):
        """
        Turns the turtle left.
        """
        self.turtle.left(5)

    def turn_right(self):
        """
        Turns the turtle right.
        """
        self.turtle.right(5)

    def clear_screen(self):
        """
        Clears the screen and resets the turtle.
        """
        self.turtle.clear()
        self.turtle.penup()
        self.turtle.home()
        self.turtle.pendown()

    def increase_speed(self):
        """
        Increases the turtle's speed.
        """
        current_speed = self.turtle.speed()
        if current_speed < 10:
            self.turtle.speed(current_speed + 1)

    def decrease_speed(self):
        """
        Decreases the turtle's speed.
        """
        current_speed = self.turtle.speed()
        if current_speed > 1:
            self.turtle.speed(current_speed - 1)

    def stop_movement(self):
        """
        Stops the turtle's movement.
        """
        self.turtle.speed(0)

    def start(self):
        """
        Starts the turtle controller's main loop.
        """
        self.screen.mainloop()


if __name__ == "__main__":
    controller = TurtleController()
    controller.start()
