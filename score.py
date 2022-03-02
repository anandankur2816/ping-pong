from turtle import Turtle


class Score(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.cpos = pos
        self.penup()
        self.wr()

    def wr(self):
        self.goto(self.cpos, 270)
        self.write(arg=f"Score:{self.score}", move=True, align="center",
                   font=("Arial", 20, "normal"))

    def update(self):
        self.score += 1
        self.clear()
        self.wr()
