from turtle import Turtle


class Playerscore(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.penup()
        self.speed(0)
        self.goto(position)
        self.color("white")
        self.hideturtle()
        self.write(
            f"{self.score}", align="center", font=("Eras Bold ITC", 50, "normal")
        )

    def incplayer1score(self):
        self.clear()
        self.score += 1
        self.write(
            f"{self.score}", align="center", font=("Eras Bold ITC", 50, "normal")
        )

    def incplayer2score(self):
        self.clear()
        self.score += 1
        self.write(
            f"{self.score}", align="center", font=("Eras Bold ITC", 50, "normal")
        )

    # def gameover(self):
    #     self.goto(0, 0)
    #     self.color("green")
    #     self.write(f"GAME OVER", align="center", font=("Eras Bold ITC", 50, "normal"))

    # def proceed(self):
    #     self.goto(0, 0)
    #     self.color("green")
    #     self.write(
    #         f"If you wish to proceed the game, then click spacebar else click esc",
    #         align="center",
    #         font=("Eras Bold ITC", 14, "normal"),
    #     )