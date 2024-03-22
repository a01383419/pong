from random import choice, random
from turtle import *
from freegames import vector

bgcolor('black')

def value():
    return (3 + random() * 2) * choice([1, -1])

def new_ball():
    return vector(0, 0), vector(value(), value())

balls = [new_ball()]
state = {1: 0, 2: 0}
score = {1: 0, 2: 0}  
speed_increment = .3  
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
    if not is_paused:  
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
                    score[2] += 1  
                    reset_ball(ball, aim)  
            
            if x > 185:
                if state[2] <= y <= state[2] + 50:
                    aim.x = -aim.x
                else:
                    score[1] += 1  
                    reset_ball(ball, aim)  
        draw_score()  
        update()
        
        if score[1] >= 10 or score[2] >= 10:
            end_game()  
        else:
            ontimer(draw, 50)  

def end_game():
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
    up()
    goto(-85, -180)
    color('white')
    write(f"{score[1]}", align="left", font=("Arial", 30, "normal"))
    goto(80, -180)
    write(f"{score[2]}", align="left", font=("Arial", 30, "normal"))
    goto(-45, 155)
    write(f"PONG", align="left", font=("Arial", 30, "normal"))

def reset_ball(ball, aim):
    ball.x, ball.y = 0, 0
    aim.x, aim.y = value(), value()

def toggle_pause():  
    global is_paused
    is_paused = not is_paused
    if not is_paused:
        draw()  


def add_ball():
    balls.append(new_ball())

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
onkey(toggle_pause, 'p') 
onkey(add_ball, 'space')  
draw()
ontimer(increase_speed, 5000)  
done()
