import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.listen()

def on_key_forward():
    tim.forward(50)
def on_key_backward():
    tim.backward(50)
def on_key_right():
    new_pos = tim.heading() +10
    tim.setheading(new_pos)

def on_key_left():
    new_pos = tim.heading() - 10
    tim.setheading(new_pos)

def on_key_clear():
    tim.clear()
    tim.penup()
    tim.reset()
    tim.pendown()



screen.onkey(key="W", fun=on_key_forward)
screen.onkey(key="S", fun=on_key_backward)
screen.onkey(key="D", fun=on_key_right)
screen.onkey(key="A", fun=on_key_left)
screen.onkey(key="C", fun=on_key_clear)

screen.exitonclick()