import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_SPEED = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    level = 0
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=2)
        self.color(random.choice(COLORS))
        self.goto(280,random.randint(-230,230))
        self.move_speed = STARTING_MOVE_SPEED
        self.calculate_speed(0)


    def move(self):
        self.setx(self.xcor()-self.move_speed)

    def remove_car(self):
        self.clear()

    def calculate_speed(self,level):
        self.move_speed = STARTING_MOVE_SPEED + (level * MOVE_INCREMENT)