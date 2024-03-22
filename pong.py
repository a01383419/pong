from random import choice, random
from turtle import *

from freegames import vector

bgcolor('black')

def value():
    return (3 + random() * 2) * choice([1, -1])

balls = [(vector(0, 0), vector(value(), value()))]  # Correction here
state = {1: 0, 2: 0}
score = {1: 0, 2: 0}
speed_increment = .5  
current_speed = 1.0  

is_paused = False

def move(player, change):
    state[player] += change

def rectangle(x, y, width, height):
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
    global current_speed

    if not is_paused:  # Only draw and move if not paused
        clear()

        color('white')
        rectangle(-200, state[1], 10, 50)
        rectangle(190, state[2], 10, 50)

        for ball, aim in balls:
            up()
            goto(ball.x, ball.y)
            dot(10, "white")

            ball.move(aim * current_speed) 
            x = ball.x
            y = ball.y

            if y < -200 or y > 200:
                aim.y = -aim.y

            if x < -185:
                if state[1] <= y <= state[1] + 50:
                    aim.x = -aim.x
                else: 
                    score[2] += 1  # Note the change here
                    aim.x = -aim.x  # Bounce off the wall
            if x > 185:
                if state[2] <= y <= state[2] + 50:
                    aim.x = -aim.x
                else:
                    score[1] += 1  # Note the change here
                    aim.x = -aim.x  # Bounce off the wall

        draw_score()  
        update()

    ontimer(draw, 50)

def draw_score():
    up()
    goto(-35, -180)
    color('white')
    write(f"{score[1]}", align="left", font=("Arial", 30, "normal"))
    goto(30, -180)
    write(f"{score[2]}", align="left", font=("Arial", 30, "normal"))
    goto(-45, 155)
    write(f"PONG", align="left", font=("Arial", 30, "normal"))

def toggle_pause():  # Create a function to toggle the pause state
    global is_paused
    is_paused = not is_paused

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: move(1, 20), 'w')
onkey(lambda: move(1, -20), 's')
onkey(lambda: move(2, 20), 'i')
onkey(lambda: move(2, -20), 'k')
onkey(toggle_pause, 'p')  # Use 'p' key to pause the game
draw()
done()