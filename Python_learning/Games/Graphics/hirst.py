import colorgram
import random
import turtle as tim
from turtle import Screen
# colors = colorgram.extract('image.jpeg', 9)
#
# out = []
# for i in range(len(colors)):
#     r = colors[i].rgb.r
#     g = colors[i].rgb.g
#     b = colors[i].rgb.b
#     new_color = (r, g, b)
#     out.append(new_color)
#
# print(out)
tim.colormode(255)
color_list = [(0, 255, 128), (0, 128, 255), (255, 51, 255), (228, 235, 231), (196, 164, 104), (141, 170, 190),
              (70, 91, 126), (217, 206, 127), (204, 204, 0)]

# to start the turtle from (0,0) location
tim.setworldcoordinates(-1, -1, tim.window_width() - 1, tim.window_height() - 1)
tim.penup()
number_of_dots = 50
incr = 0
tim.speed("fastest")
tim.hideturtle()


def check_wall():
    if tim.xcor() > 800:
        tim.penup()
        global incr
        incr = incr + 50
        tim.goto(0, incr)


for dots in range(number_of_dots+1):
    tim.forward(50)
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    check_wall()


screen = Screen()
screen.exitonclick()