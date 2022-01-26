import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

score_1 = 0
score_2 = 0
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong!")
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
player_one_score = Scoreboard((100, 240))
player_two_score = Scoreboard((-100, 240))
ball = Ball()
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
speed = 0.1
game_playing = True
while game_playing:
    screen.update()
    time.sleep(speed)

    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(r_paddle) < 60 and ball.xcor() > 320 or ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        ball.rebound()
        if speed > 0.021:
            speed -= 0.01
        print(speed)

    if ball.xcor() > 380:
        player_two_score.increase_score()
        ball.home()
        speed = 0.1
        time.sleep(1.25)

    if ball.xcor() < -380:
        player_one_score.increase_score()
        ball.home()
        speed = 0.1
        time.sleep(1.25)

screen.exitonclick()
