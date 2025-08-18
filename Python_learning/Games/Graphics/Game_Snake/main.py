import turtle
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
turtle.penup()
turtle.hideturtle()
turtle.color("white")
turtle.setposition(0,285)
turtle.write('Score: ', align='center', move=False)
screen.tracer(0)


snake = Snake()
food = Food()
score = ScoreBoard()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    screen.listen()
    snake.move()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        score.cal_score()

    # if snake hits the wall
    # if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    #     game_is_on = False
    #     turtle.goto(0,0)
    #     turtle.write("Game Over")

    # if snake hits own tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            turtle.goto(0,0)
            turtle.write("Game Over")
screen.exitonclick()
