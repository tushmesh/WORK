import turtle as tim
from turtle import Screen
import random

# colors = ["blue", "dark olive green", "tomato", "yellow", "magenta"]
movement = ["bk", "fd", "rt", "lt"]
direction = [0,90,180,270]
tim.speed("fast")
tim.colormode(255)


def color_code():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r, g, b


for _ in range(100):
    # tim.color(random.choice(colors))
    tim.color(color_code())
    tim.pensize(10)
    mov = random.choice(direction)
    tim.forward(30)
    tim.setheading(mov)


screen = Screen()
screen.exitonclick()