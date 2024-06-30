from turtle import Turtle, Screen

t = Turtle()
s = Screen()

s.setup(width=600, height=600)


def move_fd():
    t.fd(20)


def move_bk():
    t.fd(-20)


def move_left():
    t.left(5)


def move_right():
    t.right(5)


s.listen()
s.onkey(move_fd, "Up")
s.onkey(move_bk, "Down")
s.onkey(move_left, "Left")
s.onkey(move_right, "Right")

s.mainloop()
