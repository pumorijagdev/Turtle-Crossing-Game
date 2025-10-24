import time
from turtle import Screen
from Player import Player
from CarManager import CarManager
from Scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_car()

    # detect collision of turtle with car
    for one_car in car.all_cars:
        if one_car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
        
    # reaches finish line or not
    if player.is_at_finish_line():
        player.go_to_start()
        car.level_up()
        scoreboard.increase_level()

screen.exitonclick()