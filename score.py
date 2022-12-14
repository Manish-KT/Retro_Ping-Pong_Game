from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-50, 220)
        self.write(self.l_score, align="center", font=("courier", 50, "normal"))
        self.goto(50, 220)
        self.write(self.r_score, align="center", font=("courier", 50, "normal"))

    def new_score(self):
        self.goto(-50, 220)
        self.write(self.l_score, align="center", font=("courier", 50, "normal"))
        self.goto(50, 220)
        self.write(self.r_score, align="center", font=("courier", 50, "normal"))

    def left_score(self):
        self.l_score += 1
        self.clear()
        self.new_score()

    def right_score(self):
        self.r_score += 1
        self.clear()
        self.new_score()