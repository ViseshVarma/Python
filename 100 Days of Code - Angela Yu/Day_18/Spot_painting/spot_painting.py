import turtle as t
import random
from turtle import Screen
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)

color_list = [(248, 246, 236), (237, 250, 244), (251, 239, 248), (236, 243, 250), (233, 222, 92), (211, 158, 105),
              (116, 177, 210),
              (226, 57, 131), (181, 78, 33), (210, 135, 174), (41, 103, 161), (12, 21, 62), (184, 46, 111),
              (186, 164, 23),
              (43, 182, 112), (122, 187, 155), (25, 32, 158), (173, 16, 67), (234, 164, 199), (229, 75, 43),
              (22, 179, 205),
              (11, 41, 23), (49, 126, 73), (146, 218, 196), (51, 21, 11), (227, 220, 10), (106, 95, 206),
              (133, 215, 229),
              (175, 177, 227), (59, 16, 31)]

t.colormode(255)
t.shape("turtle")
t.color("Blue")
t.pensize(20)
t.speed(0)

t.penup()
t.setheading(225)
t.forward(300)
t.left(135)

dot_count = 100

for i in range(1, dot_count + 1):
    t.dot(10, random.choice(color_list))
    t.penup()
    t.forward(50)
    t.pendown()

    if i % 10 == 0:
        t.left(90)
        t.penup()
        t.forward(50)
        t.left(90)
        t.forward(500)
        t.right(180)
        t.pendown()

screen = Screen()
screen.exitonclick()
