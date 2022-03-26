from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.next_level()

    def next_level(self):
        self.clear()
        self.write(f"Level:{self.level}", align="left", font=FONT)
        self.level += 1

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)
