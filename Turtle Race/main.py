from turtle import Turtle, Screen
import random


def main():
    # Create a screen
    s = Screen()
    s.setup(width=600, height=600)

    # List of colors to shuffle
    colors = ['red', 'green', 'blue', 'brown', 'purple', 'pink']
    random.shuffle(colors)

    # Create six turtles
    turtles = []
    start_y = -125  # Starting y-position for the first turtle
    spacing = 50     # Spacing between turtles

    for color in colors:
        new_turtle = Turtle()
        new_turtle.shape('turtle')
        new_turtle.color(color)
        new_turtle.penup()  # Lift the pen to avoid drawing lines
        new_turtle.setpos(-285, start_y)
        start_y += spacing
        turtles.append(new_turtle)

    # Hide the original turtle cursor
    # s.tracer(False)  # Turn off screen updates temporarily
    # for turtle in turtles:
    #     turtle.stamp()  # Stamp each turtle onto the screen
    # s.tracer(True)   # Turn on screen updates
    cnt = 0
    while True:
        for i in turtles:
            if cnt % 5 == 0:
                i.speed(random.choice([0, 10, 6, 3, 1]))
            if i.xcor() >= 280:
                print(f"{i.color()} wins")
                return
        turtles[0].fd(10)
        turtles[1].fd(10)
        turtles[2].fd(10)
        turtles[3].fd(10)
        turtles[4].fd(10)
        turtles[5].fd(10)
        cnt += 1

    # Keep the window open until it's closed by the user
    # s.mainloop()


if __name__ == '__main__':
    main()
