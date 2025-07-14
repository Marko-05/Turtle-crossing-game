import time
import sys
import os
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random
from PIL import Image

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
background = Image.open(resource_path("background.png"))

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")

screen.tracer(0)
screen.bgpic(background.filename)
timmy = Player()
score = Scoreboard()

screen.listen()
screen.onkeypress(timmy.moveup, "w")
screen.onkeypress(timmy.moveup, "W")

canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
game_is_on = True
car_list = []
exit_check = 0

while game_is_on:

    def on_close():
        global exit_check
        exit_check = 1


    root.protocol("WM_DELETE_WINDOW", on_close)

    if exit_check == 1:
        sys.exit()

    else:
        time.sleep(0.1)
        screen.update()
        if random.randint(1,10) >= 8:
            new_car = CarManager()
            car_list.append(new_car)

        for car in car_list:
            car.calculate_speed(score.level-1)
            car.move()
            if car.xcor() < -300:
                car.remove_car()

            if timmy.distance(car) < 15:
                game_is_on = False
                score.game_over()

        if timmy.ycor() > 280:
            score.update_score()
            timmy.reset_pos()



#This part of the code solves the issue where the X button stops working during the GAME OVER screen
def shutoff():
    sys.exit()

root.protocol("WM_DELETE_WINDOW", shutoff)
screen.exitonclick()
shutoff()