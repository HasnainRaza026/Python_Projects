from turtle import Turtle,  Screen

t = Turtle()
s = Screen()

s.setup(width=350, height=350)
for _ in range(10):
    t.pendown()
    t.fd(5)
    t.penup()
    t.fd(5)


s.mainloop()
