# Documentación en el readme

# Importación de módulos necesarios para el juego
from random import choice, random
from turtle import *
from freegames import vector

# Configuración inicial de la pantalla del juego
bgcolor('black')

def value():
    """Genera un valor aleatorio para la velocidad y dirección de la bola."""
    return (3 + random() * 2) * choice([1, -1])

def new_ball():
    """Crea una nueva bola con posición y velocidad iniciales."""
    return vector(0, 0), vector(value(), value())

# Inicialización de variables del estado del juego
balls = [new_ball()]
state = {1: 0, 2: 0}
score = {1: 0, 2: 0}
speed_increment = .3
current_speed = 1.0
is_paused = False

def move(player, change):
    """Actualiza la posición de la paleta del jugador."""
    state[player] += change

def rectangle(x, y, width, height):
    """Dibuja un rectángulo en la pantalla."""
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
    """Dibuja todos los elementos del juego en la pantalla y actualiza el estado del juego."""
    global current_speed
    if not is_paused:
        clear()

        # Dibujo de las paletas y la bola
        color('white')
        rectangle(-200, state[1], 10, 50)
        rectangle(190, state[2], 10, 50)

        for ball, aim in balls:
            up()
            goto(ball.x, ball.y)
            dot(10, "white")

            # Actualización de la posición de la bola
            ball.move(aim * current_speed)
            # Revisa colisiones y actualiza la dirección de la bola
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
        # Dibuja el marcador y actualiza la pantalla
        draw_score()
        update()

        # Revisa si el juego ha terminado y programa el próximo dibujo
        if score[1] >= 10 or score[2] >= 10:
            end_game()
        else:
            ontimer(draw, 50)

def end_game():
    """Finaliza el juego mostrando el ganador."""
    clear()
    up()
    goto(0, 0)
    color('white')
    if score[1] > score[2]:
        write("Player 1 wins", align="center", font=("Arial", 30, "normal"))
    else:
        write("Player 2 wins", align="center", font=("Arial", 30, "normal"))
    update()

def draw_score():
    """Dibuja el marcador en la pantalla."""
    up()
    goto(-85, -180)
    color('white')
    write(f"{score[1]}", align="left", font=("Arial", 30, "normal"))
    goto(80, -180)
    write(f"{score[2]}", align="left", font=("Arial", 30, "normal"))
    goto(-45, 155)
    write(f"PONG", align="left", font=("Arial", 30, "normal"))

def reset_ball(ball, aim):
    """Reinicia la posición y velocidad de la bola."""
    ball.x, ball.y = 0, 0
    aim.x, aim.y = value(), value()

def toggle_pause():
    """Alterna el estado de pausa del juego."""
    global is_paused
    is_paused = not is_paused
    if not is_paused:
        draw()  # Continúa el dibujo/actualización del juego si se despausa.

def add_ball():
    """Agrega una nueva bola al juego con posición y velocidad iniciales."""
    balls.append(new_ball())

def increase_speed():
    """Incrementa la velocidad actual del juego."""
    global current_speed
    current_speed += speed_increment

# Configuración inicial de la ventana del juego y eventos de teclado
title("PONG2 - EQ10")
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()

# Asignación de teclas para controlar las paletas y otras funcionalidades del juego
onkey(lambda: move(1, 20), 'w')  # Mueve la paleta del jugador 1 hacia arriba
onkey(lambda: move(1, -20), 's')  # Mueve la paleta del jugador 1 hacia abajo
onkey(lambda: move(2, 20), 'i')  # Mueve la paleta del jugador 2 hacia arriba
onkey(lambda: move(2, -20), 'k')  # Mueve la paleta del jugador 2 hacia abajo
onkey(toggle_pause, 'p')  # Alterna el estado de pausa del juego
onkey(add_ball, 'space')  # Agrega una nueva bola al juego

# Inicio del juego
draw()  # Llama a la función de dibujo para iniciar el juego
ontimer(increase_speed, 5000)  # Programa incrementos de velocidad cada 5000 ms
done()  # Finaliza la configuración de Turtle

