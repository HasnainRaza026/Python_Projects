from turtle import Turtle, Screen
import random

t = Turtle()
s = Screen()


def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


s.setup(width=600, height=600)
t.speed(0)
s.colormode(255)

for i in range(1, 50):
    t.pencolor(random_color())
    t.setheading(i*7.2)
    t.circle(100)

s.mainloop()
