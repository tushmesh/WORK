import time
import turtle
from turtle import Screen

import player
from player import Player
from cars import Cars
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
cars = Cars()
player = Player()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
game_is_on = True
screen.listen()
screen.onkey(player.move_up, "Up")


while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.display_car()
    cars.move_cars()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            print("Game Over")
            game_is_on = False


