from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


def close_programme():
    scr.bye()


scr = Screen()
scr.setup(width=800, height=600)
scr.bgcolor("black")
scr.title("Pong")
scr.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

scr.listen()
scr.onkey(close_programme, "Escape")
scr.onkey(r_paddle.go_up, "Up")
scr.onkey(r_paddle.go_down, "Down")
scr.onkey(l_paddle.go_up, "w")
scr.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    scr.update()
    ball.move()

    # Wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Paddle collision
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Score update left player
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Score update right player
    if ball.xcor() < - 380:
        ball.reset_position()
        scoreboard.r_point()

scr.exitonclick()
