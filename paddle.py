from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.speed("fastest")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(position)
        self.ycor()

    def up(self):
        if self.ycor() < 260:
            self.forward(20)

    def down(self):
        if self.ycor() > -240:
            self.back(20)
