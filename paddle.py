from turtle import Turtle

distance_moved = 60


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.create_paddle(pos)

    def create_paddle(self, pos):
        self.speed(0)
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(5, 1)
        self.goto(pos, 0)

    def up(self):
        y = self.pos()[1] + distance_moved
        x = self.pos()[0]
        self.goto(x, y)

    def down(self):
        y = self.pos()[1] - distance_moved
        x = self.pos()[0]
        self.goto(x, y)
