import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    ran_color = (r, g, b)
    return ran_color


directions = [0, 90, 180, 270]
tim.speed(0)

for i in range(72):
    tim.color(random_color())
    tim.circle(100)
    tim.right(5)

screen = Screen()
screen.exitonclick()
