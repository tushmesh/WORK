import turtle
from turtle import Screen
from pongshape import PongShape
from ball import  MoveBall
from scoreboard import ScoreBoard

screen = Screen()
scoreboard = ScoreBoard()
screen.title("Pong")
screen.setup(width=600, height=600)
screen.bgcolor("black")
game_is_on = True
screen.tracer()
screen.listen()

r_paddle = PongShape((280, 0))
l_paddle = PongShape((-280, 0))

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
ball = MoveBall()
while game_is_on:
    ball.ball_move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 250 or ball.distance(l_paddle) < 35 and ball.xcor() > -300:
        ball.bounce_x()

    if ball.xcor() > 305:
        scoreboard.l_point()
        ball.reset_position()
    if ball.xcor() < -305:
        scoreboard.r_point()
        ball.reset_position()
screen.exitonclick()

