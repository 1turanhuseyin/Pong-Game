import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

line = Turtle()
line.color("SkyBlue")
line.hideturtle()
line.pensize(4)
line.setheading(37)
line.penup()
line.forward(492)
line.setheading(180)
line.pendown()
line.forward(800)
line.penup()
line.setheading(270)
line.forward(585)
line.setheading(0)
line.pendown()
line.color("SkyBlue")
line.forward(800)

right_paddle = Paddle((370, 0))
left_paddle = Paddle((-370, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=right_paddle.move_up_paddle, key="Up")
screen.onkeypress(fun=right_paddle.move_down_paddle, key="Down")

screen.onkeypress(fun=left_paddle.move_up_paddle, key="w")
screen.onkeypress(fun=left_paddle.move_down_paddle, key="s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 288 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 350 or ball.xcor() < -350:
        if ball.distance(right_paddle) < 51 or ball.distance(left_paddle) < 51:
            ball.bounce_x()

    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()
        screen.update()
        time.sleep(1)

    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()
        screen.update()
        time.sleep(1)





screen.exitonclick()