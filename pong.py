from random import choice, random
from turtle import *

from freegames import vector

# Define global variables
def value():
    """Randomly generate value between (-5, -3) or (3, 5)."""
    return (3 + random() * 2) * choice([1, -1])

ball = vector(0, 0)
aim = vector(value(), value())
stateS = {1: 0, 2: 0}  # Dictionary to hold scores for players 1 and 2
stateP = {1: 0, 2: 0}  # Dictionary to hold paddle positions for players 1 and 2


def move(player, change):
    """Move player position by change."""
    # Move the player only if it won't go out of bounds
    if -190 <= stateP[player] + change <= 140:
        stateP[player] += change


def rectangle(x, y, width, height):
    """Draw rectangle at (x, y) with given width and height."""
    up()
    goto(x, y)
    down()
    begin_fill()
    for _ in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()


def draw():
    """Draw game and move pong ball."""
    clear()
    # Draw the left and right walls
    rectangle(-215, -215, 10, 430)  # Left wall
    rectangle(205, -215, 10, 430)   # Right wall
    
    # Draw the paddles
    rectangle(-200, stateP[1], 10, 50)
    rectangle(190, stateP[2], 10, 50)

    ball.move(aim)
    x = ball.x
    y = ball.y

    up()
    goto(x, y)
    dot(10)
    update()

    # Check if the ball hits the top or bottom wall
    if y < -190 or y > 190:
        aim.y = -aim.y

    # Check if the ball hits the left wall
    if x < -199:
        low = stateS[1]
        high = stateS[1] + 50

        # Check if the ball is within the paddle's range
        if low <= y <= high:
            aim.x = -aim.x
        else:
            # Player 2 scores
            stateS[2] += 1
            aim.x = -aim.x

    # Check if the ball hits the right wall
    if x > 199:
        low = stateS[2]
        high = stateS[2] + 50

        # Check if the ball is within the paddle's range
        if low <= y <= high:
            aim.x = -aim.x
        else:
            # Player 1 scores
            stateS[1] += 1
            aim.x = -aim.x

    # Display scores
    goto(0, 200)
    write(f"Player 1: {stateS[1]}   Player 2: {stateS[2]}", align="center", font=("Roboto", 14, "bold"))

    ontimer(draw, 50)


setup(440, 440, 370, 0)  # Increased window size
title("Pong")  # Set window title
hideturtle()
tracer(False)
listen()
onkey(lambda: move(1, 20), 'w')
onkey(lambda: move(1, -20), 's')
onkey(lambda: move(2, 20), 'i')
onkey(lambda: move(2, -20), 'k')
draw()
done()