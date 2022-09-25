from turtle import Turtle


class Paddle:

    def __init__(self):
        self.segment = []
        self.left = 0
        self.right = 0

    def create_paddle(self):
        for i in range(2):
            torti = Turtle()
            torti.penup()
            torti.color("white")
            torti.speed("fastest")
            torti.shape("square")
            torti.turtlesize(stretch_wid=5, stretch_len=1)
            self.segment.append(torti)

        self.segment[0].goto(430, 0)
        self.segment[1].goto(-430, 0)

    def left_up(self):
        if self.left < 295:
            self.left = self.left + 20
            self.segment[0].goto(430, self.left)

    def left_down(self):
        if self.left > -295:
            self.left = self.left - 20
            self.segment[0].goto(430, self.left)

    def right_up(self):
        if self.right < 295:
            self.right = self.right + 20
            self.segment[1].goto(-430, self.right)

    def right_down(self):
        if self.right > -295:
            self.right = self.right - 20
            self.segment[1].goto(-430, self.right)

