import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.move_player, "Up")

car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.move_cars()
    if player.is_at_finish_line():
        # Reset player to bottom of screen
        player.go_to_start()
        # Level up - Increase car speed
        car_manager.level_up()
        # Add to score
        scoreboard.user_score()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()