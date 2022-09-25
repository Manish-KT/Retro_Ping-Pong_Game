from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

# 1. create a screen
paddle = Paddle()
ball = Ball()
screen = Screen()
scoreboard = Scoreboard()
speed = 0.05
# ball.boundary()

screen.bgcolor("black")
screen.setup(width=900, height=610)
screen.title("Retro Ping-Pong Game :>)")

# 2. create and move a paddle.
paddle.create_paddle()
screen.listen()
screen.onkey(paddle.left_up, "Up")
screen.onkey(paddle.left_down, "Down")
screen.onkey(paddle.right_up, "w")
screen.onkey(paddle.right_down, "s")

# 3. detect collision with ball
game_on = True
ball.make_ball()

while game_on:
    time.sleep(speed)
    screen.update()
    ball.start()
    if ball.ball_y > 280 or ball.ball_y < -280:
        ball.bounce_y()
    # 4. detect collision with right paddle
    # 5. detect collision when paddle misses
    if ball.ball_x > 400 or ball.ball_x < -400:
        if ball.torti.distance(paddle.segment[0]) < 60:
            ball.bounce_x()
            scoreboard.right_score()
            speed *= 0.9

        elif ball.torti.distance(paddle.segment[1]) < 60:
            ball.bounce_x()
            scoreboard.left_score()
            speed *= 0.9

        else:
            ball.reset()
            speed = 0.05


# 6. keep track of score
screen.exitonclick()
