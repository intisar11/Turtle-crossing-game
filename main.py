import time
from turtle import Screen
from player import Player
from car_manager import Car
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=600, height= 600)
screen.tracer(0)

player = Player()
cars = Car()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move,'Up')



game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_car()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
    if player.is_at_finish_line():
        player.reset_position()










screen.exitonclick()