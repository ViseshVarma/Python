from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()

# creating the boundary
screen.bgcolor("black")
screen.screensize(canvwidth=800, canvheight=600)
screen.title("Pong")
screen.tracer(0)

# creating paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Listening to key input from user
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# to keep refreshing the screen. when tracer is 0,
# if the below code is not written then the paddle will not show up.
game_is_on = True
while game_is_on:
    screen.update()

# To exit from the game when any part of the window is clicked
screen.exitonclick()
