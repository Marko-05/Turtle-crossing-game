from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("chartreuse")
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.setheading(90)

    def moveup(self):
        self.sety(self.ycor()+MOVE_DISTANCE)

    def reset_pos(self):
        self.goto(STARTING_POSITION)
