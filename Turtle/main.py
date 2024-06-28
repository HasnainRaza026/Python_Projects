import turtle
import random

# Create a turtle screen
screen = turtle.Screen()
screen.setup(width=600, height=600)  # Set up the screen size

# Create a turtle instance
t = turtle.Turtle()

# Hide the turtle (optional)
t.hideturtle()

# Set the speed of the turtle
t.speed(0)  # Fastest

# Function to generate a random color


def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Function to draw a grid of dots


def draw_dot_pattern(rows, cols, dot_size, spacing):
    screen.colormode(255)  # Set the color mode to 255 to use RGB values

    # Calculate the starting position (bottom left)
    start_x = -screen.window_width() // 2 + spacing // 2
    start_y = -screen.window_height() // 2 + spacing // 2

    for row in range(rows):
        for col in range(cols):
            t.penup()
            t.goto(start_x + col * spacing, start_y + row * spacing)
            t.pendown()
            t.dot(dot_size, random_color())


# Draw a pattern of 10x10 dots
draw_dot_pattern(10, 10, 20, 30)

# Close the turtle graphics window on click
screen.exitonclick()
