from random import choice, random
from turtle import *
from freegames import vector

# Set the background color to black
bgcolor('black')

def value():
    """Randomly generate value between (-5, -3) or (3, 5)."""
    return (3 + random() * 2) * choice([1, -1])

# Function to create a new ball
def new_ball():
    return vector(0, 0), vector(value(), value())

# Initial setup with one ball
balls = [new_ball()]
state = {1: 0, 2: 0}
score = {1: 0, 2: 0}  # Add a score counter for each player
speed_increment = .3  # Incremental speed increase over time
current_speed = 1.0  # Initial speed
is_paused = False

def move(player, change):
    """Move player position by change."""
    state[player] += change

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
    """Draw game and move pong balls."""
    global current_speed
    if not is_paused:  # Only draw and move if not paused
        clear()
        # Draw players with white color
        color('white')
        rectangle(-200, state[1], 10, 50)
        rectangle(190, state[2], 10, 50)
        # Draw the balls
        for ball, aim in balls:
            up()
            goto(ball.x, ball.y)
            dot(10, "white")
            # Move the ball
            ball.move(aim * current_speed)  # Multiply aim by current speed
            x = ball.x
            y = ball.y
            # Check if ball touches the wall and bounce
            if y < -200 or y > 200:
                aim.y = -aim.y
            # Check if ball touches the left wall
            if x < -185:
                if state[1] <= y <= state[1] + 50:
                    aim.x = -aim.x
                else:
                    score[2] += 1  # Update player 2 score
                    reset_ball(ball, aim)  # Reset ball position and direction
            # Check if ball touches the right wall
            if x > 185:
                if state[2] <= y <= state[2] + 50:
                    aim.x = -aim.x
                else:
                    score[1] += 1  # Update player 1 score
                    reset_ball(ball, aim)  # Reset ball position and direction
        draw_score()  # Update the score
        update()
        # Check if any player has reached 10 points
        if score[1] >= 10 or score[2] >= 10:
            end_game()  # Call the function to end the game
        else:
            ontimer(draw, 50)  # Recursive call to keep updating the game

def end_game():
    """End the game."""
    clear()
    up()
    goto(0, 0)
    color('white')
    if score[1] > score[2]:
        write("Player 1 wins", align="center", font=("Arial", 30, "normal"))
    else:
        write("Player 2 wins", align="center", font=("Arial", 30, "normal"))
    update()
    done()

def draw_score():
    """Draw the score for each player."""
    up()
    goto(-35, -180)
    color('white')
    write(f"{score[1]}", align="left", font=("Arial", 30, "normal"))
    goto(30, -180)
    write(f"{score[2]}", align="left", font=("Arial", 30, "normal"))
    goto(-45, 155)
    write(f"PONG", align="left", font=("Arial", 30, "normal"))

def reset_ball(ball, aim):
    """Reset ball position and direction."""
    ball.x, ball.y = 0, 0
    aim.x, aim.y = value(), value()

def toggle_pause():  # Create a function to toggle the pause state
    global is_paused
    is_paused = not is_paused

# Function to add a new ball
def add_ball():
    balls.append(new_ball())

# Function to increase speed
def increase_speed():
    global current_speed
    current_speed += speed_increment

title("PONG2 - EQ10")
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: move(1, 20), 'w')
onkey(lambda: move(1, -20), 's')
onkey(lambda: move(2, 20), 'i')
onkey(lambda: move(2, -20), 'k')
onkey(toggle_pause, 'p')  # Use 'p' key to pause the game
onkey(add_ball, 'space')  # Use 'space' key to add a new ball
draw()
ontimer(increase_speed, 5000)  # Increase speed every 5 seconds
done()