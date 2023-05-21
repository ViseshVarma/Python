import random
import turtle as t
from turtle import Screen

tim = t.Turtle()

colors = ["bisque", "Grey", "blue", "red", "aquamarine", "indigo", "plum", "cyan", "orchid"]
no_of_sides = 5


def draw_shape(no_of_sides):
    angle = 360 / no_of_sides
    for i in range(no_of_sides):
        tim.color(random.choice(colors))
        tim.forward(100)
        tim.right(angle)


for shape in range(3, 11):
    draw_shape(shape)


screen = Screen()
screen.exitonclick()
