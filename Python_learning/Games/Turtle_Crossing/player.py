import turtle
import random
from cars import Cars
from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
CAR_START_POSITION = (280,0)
cars = Cars()


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.right(-90)

    def move_up(self):
        if self.ycor() <= 280:
            move_forward = self.ycor() + 10
            self.goto(0, move_forward)
            #self.forward(MOVE_DISTANCE)
        else:
            print("You Won !")













