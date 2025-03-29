from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.ycorextra = 1
        self.xcorextra = 1

    def ballmove(self):
        self.goto(
            self.xcor() + 10 * (self.xcorextra), self.ycor() + 10 * (self.ycorextra)
        )

    def collision(self):
        self.ycorextra *= -1

    def collision_with_paddle(self):
        if self.ycorextra == 1 and self.xcorextra == -1:
            self.xcorextra = 1
        if self.ycorextra == -1 and self.xcorextra == 1:
            self.xcorextra *= -1

    def resetball(self):
        self.goto(0, 0)
        self.ycorextra *= -1
        self.xcorextra *= -1
        self.ballmove()