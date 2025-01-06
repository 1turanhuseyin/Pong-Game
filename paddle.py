WIDTH = 20
HEIGHT = 100

from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=HEIGHT / 20, stretch_len=WIDTH / 20)
        self.penup()
        self.goto(position)
        self.paddle_speed = 20

    def move_up_paddle(self):
        self.sety(self.ycor() + self.paddle_speed)

    def move_down_paddle(self):
        self.sety(self.ycor() - self.paddle_speed)

