from turtle import Turtle

FONT = ("Courier", 22, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.level = 0
        self.hideturtle()
        self.update_score()


    def update_score(self):
        self.level += 1
        self.clear()
        self.goto(-210, 260)
        self.write(f"Level: {self.level}",font=FONT, align="center")

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
