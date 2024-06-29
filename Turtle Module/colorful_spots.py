import turtle
import random

screen = turtle.Screen()
screen.setup(width=350, height=350)

timmy = turtle.Turtle()
timmy.speed(0)


def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def turtle_position():
    return -screen.window_width() // 2 + 20, -screen.window_height() // 2 + 25


def draw_dot_pattern(rows, cols, dot_size, spacing):
    screen.colormode(255)
    start_x, start_y = turtle_position()
    start_x = start_x + spacing // 2
    start_y = start_y + spacing // 2

    for row in range(rows):
        for col in range(cols):
            timmy.penup()
            timmy.goto(start_x + col * spacing, start_y + row * spacing)
            timmy.pendown()
            timmy.dot(dot_size, random_color())


draw_dot_pattern(10, 10, 20, 30)

screen.mainloop()
