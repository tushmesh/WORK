import random
import turtle
from turtle import Turtle

START_POSITION = (100, 150)


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.xpos = 280

    def display_car(self):
        random_chance = random.randint(1,5)

        if random_chance == 1:
            self.car_colors = ["red", "white", "purple", "green"]
            new_car = Turtle("square")
            y = random.randint(-250,250)
            new_car.goto(280,y)
            new_car.color(random.choice(self.car_colors))
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            y_cor = new_car.position()[1]
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(5)


