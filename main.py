from turtle import Screen
import time

from ball import Ball
from paddle import Paddle

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('pong')
Screen().tracer(0)


r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()


screen.listen()
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")

game_is_on = True
while game_is_on:
    ball.move()
    screen.update()
    time.sleep(0.2)

screen.exitonclick()
