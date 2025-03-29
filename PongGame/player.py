from turtle import Turtle


class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=3, stretch_len=1)
        self.speed("fastest")
        self.penup()
        self.goto(position)

    def forward(self):
        self.penup()
        self.goto(self.xcor(), self.ycor() + 40)

    def backward(self):
        self.penup()
        self.goto(self.xcor(), self.ycor() - 40)