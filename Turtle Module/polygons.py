from turtle import Turtle, Screen
import random

t = Turtle()
s = Screen()

s.setup(width=600, height=600)


def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def turtle_position():
    return -s.window_width() // 12, s.window_height() // 4


s.colormode(255)
t.penup()
t.goto(turtle_position())
t.pendown()

for i in range(3, 11):
    n = (i-2)*180 / i
    t.pencolor(random_color())
    for _ in range(i):
        t.fd(100)
        t.right(180-n)

s.mainloop()
