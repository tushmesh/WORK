import turtle as tim
import random
from turtle import Screen

tim.colormode(255)

def color_code():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color


tim.speed("fastest")
def spirograph(gap_size):
    for _ in range(int(360/gap_size)):
        tim.color(color_code())
        tim.circle(60)
        # tim.left(10)
        tim.setheading(tim.heading() + gap_size)

spirograph(5)
screen = Screen()
screen.exitonclick()