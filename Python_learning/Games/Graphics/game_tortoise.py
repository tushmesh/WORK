import turtle as t
from turtle import Screen
import random


def pick_color():
    colors = ["blue", "black", "brown", "red", "yellow", "green", "orange", "beige", "turquoise", "pink"]
    random.shuffle(colors)
    return colors[0]


def shapes (num):
    angle = 360 / num
    for _ in range(num):
        t.forward(100)
        t.right(angle)


colors = ["blue", "dark olive green", "tomato", "yellow", "magenta"]
side_list = [3,4,5,6,7,8,9]

for i in side_list:
    t.color(random.choice(colors))
    shapes(i)

# Square
# for _ in range(2):
#     pick_color()
#     t.forward(40)
#     t.right(rotation/4)
#     t.forward(40)
#     t.right(rotation/4)
# # # Triangle
# for _ in range(1):
#     t.color("red")
#     t.forward(40)
#     t.right(rotation/3)
#     t.forward(40)
#     t.right(rotation/3)
#     t.forward(40)
# # Pentagon
# for _ in range(1):
#     pick_color()
#     t.right(120)
#     t.forward(60)
#     t.right(72)
#     t.forward(60)
#     t.right(72)
#     t.forward(60)
#     t.right(72)
#     t.forward(60)
#     t.right(72)
#     t.forward(60)


#
screen = Screen()
screen.exitonclick()
