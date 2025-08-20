from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game by TrickyLoop")
screen.tracer(0)

# Objects
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
 
screen.listen()
screen.onkeypress(key="Up", fun=r_paddle.up)
screen.onkeypress(key="Down", fun=r_paddle.down)
screen.onkeypress(key="w", fun=l_paddle.up)
screen.onkeypress(key="s", fun=l_paddle.down)

game_is_on = True

while game_is_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if (ball.distance(r_paddle) < 63 and ball.xcor() == 330) or (ball.distance(l_paddle) < 63 and ball.xcor() == -330):
        ball.bounce_x()

    # Detect r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_l_score()
    
    # Detect l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_r_score()
