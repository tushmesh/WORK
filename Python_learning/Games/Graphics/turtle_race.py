import turtle
from turtle import Turtle, Screen
import random

game_started = False
screen = Screen()
new_turtle = Turtle()
colors = ["red", "black", "brown", "pink", "yellow", "green"]
ypos = [-70, -40, -10, 30, 60, 90]
all_turtle = []
screen.setup(width=600, height=500)
bet = turtle.textinput("Bet on Color", "Choose the color: ")

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-280, y=ypos[i])
    all_turtle.append(new_turtle)

if bet in colors:
    game_started = True
else:
    print("Choose the proper color")
while game_started:
    for turtles in all_turtle:
        if turtles.xcor() > 265:
            winning_color = turtles.pencolor()
            game_started = False
            if winning_color == bet:
                print(f"You won the race. The {winning_color} won the race ")
            else:
                print(f"You Loose the race. The {winning_color} won the race ")
        move_fwd = random.randint(0, 10)
        turtles.forward(move_fwd)
screen.exitonclick()
