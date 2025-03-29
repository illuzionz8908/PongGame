from turtle import Turtle


class Dash(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pensize(7)
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(0, -300)
        self.pendown()
        self.setheading(90)
        self.draw()

    def draw(self):
        for i in range(12):
            self.pendown()
            self.fd(40)
            self.penup()
            self.fd(10)

from turtle import Screen, Turtle
from dash import  Dash
from player import Player
from playerscore import Playerscore
from ball import Ball
import time

screen = Screen()
player1score = Playerscore((-100, 220))
player2score = Playerscore((100, 220))

score_text = Turtle()
score_text.hideturtle()
score_text.penup()
score_text.color("white")  
score_text.goto(-380, 235)  
score_text.write("Score:", align="left", font=("Eras Bold ITC", 30, "normal"))

player1 = Player((-350, 0))

# we dont need to make two files for player 1 and player2, we could just make a player file and change the coord in the mian class

player2 = Player((350, 0))

ball = Ball()
dash = Dash()
screen.bgcolor("red")
screen.setup(height=600, width=800)
screen.title("Pong Game")
screen.tracer(0)

screen.listen()
screen.onkey(player1.forward, "w")
screen.onkey(player1.backward, "s")
screen.onkey(player2.forward, "o")
screen.onkey(player2.backward, "l")


gameon = True
while gameon:
    time.sleep(0.035)
    screen.update()
    ball.ballmove()

    if ball.xcor() == 390:
        player1score.incplayer1score()
        ball.resetball()

    if ball.xcor() == -390:
        player2score.incplayer2score()
        ball.resetball()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.collision()

    if ball.xcor() <= -340:
        if ball.distance(player1) < 60:
            ball.collision_with_paddle()
    if ball.xcor() >= 340:
        if ball.distance(player2) < 60:
            ball.collision_with_paddle()
screen.exitonclick()