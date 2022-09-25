from turtle import Turtle


class Ball:

    def __init__(self):
        self.ball_x = 0
        self.ball_y = 0
        self.x = 10
        self.y = 10
        self.torti = Turtle()

    def make_ball(self):
        self.torti.shape("circle")
        self.torti.penup()
        self.torti.speed(2)
        self.torti.color("white")
        self.torti.goto(self.ball_x, self.ball_y)

    def start(self):
        self.ball_x += self.x
        self.ball_y += self.y
        self.torti.goto(self.ball_x, self.ball_y)

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1

    def reset(self):
        self.torti.hideturtle()
        self.ball_x = self.ball_y = 0
        self.torti.goto(self.ball_x, self.ball_y)
        self.torti.showturtle()
        self.bounce_x()

    # def boundary(self):
    #     t2 = Turtle()
    #     t2.width = 5
    #     t2.penup()
    #     t2.goto(-455, -310)
    #     t2.pendown()
    #     t2.goto(-455, 310)
    #     t2.goto(455, 310)
    #     t2.goto(455, -310)
    #     t2.goto(-455, -310)
    #     t2.hideturtle()




