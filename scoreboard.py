from turtle import Turtle, Screen

screen = Screen()
FONT = ("Courier", 50, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.goto(position)
        self.write(self.score, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(self.score, align=ALIGNMENT, font=FONT)
