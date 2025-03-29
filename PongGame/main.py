from turtle import Screen, Turtle
from ball import Ball
from dash import Dash
from player import Player
from playerscore import Playerscore
import time

# Set up the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong Game")
screen.tracer(0)  # Turn off auto-refresh for smooth animation

# Create game elements
player1 = Player((-350, 0))  # Left paddle
player2 = Player((350, 0))   # Right paddle
ball = Ball()
dash = Dash()

# Scoreboards
player1score = Playerscore((-100, 220))  # Position for player 1's score
player2score = Playerscore((100, 220))   # Position for player 2's score

# Static "Score" text display
score_text = Turtle()
score_text.hideturtle()
score_text.penup()
score_text.color("white")
score_text.goto(-380, 235)
score_text.write("Score:", align="left", font=("Arial", 24, "normal"))

# Player controls
screen.listen()
screen.onkey(player1.forward, "w")    # W key moves Player 1 up
screen.onkey(player1.backward, "s")  # S key moves Player 1 down
screen.onkey(player2.forward, "o")    # O key moves Player 2 up
screen.onkey(player2.backward, "l")  # L key moves Player 2 down

# Main game loop
gameon = True
while gameon:
    time.sleep(0.035)  # Control game speed
    screen.update()    # Refresh the screen
    ball.ballmove()    # Move the ball

    # Ball collision with top/bottom walls
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.collision()

    # Ball collision with paddles
    if ball.xcor() <= -340 and ball.distance(player1) < 60:
        ball.collision_with_paddle()
    if ball.xcor() >= 340 and ball.distance(player2) < 60:
        ball.collision_with_paddle()

    # Ball goes out of bounds on the left (Player 2 scores)
    if ball.xcor() <= -390:
        player2score.incplayer2score()
        ball.resetball()

    # Ball goes out of bounds on the right (Player 1 scores)
    if ball.xcor() >= 390:
        player1score.incplayer1score()
        ball.resetball()

# Exit on click
screen.exitonclick()