# **Juego de Pong en Python**
Esta es una versión modificada del clásico juego Pong implementado en Python utilizando el módulo Turtle. En esta versión, se han agregado características y modificaciones adicionales para mejorar la jugabilidad.

## **Características:**
- **Dos Jugadores:** ¡Juega contra un amigo o contra ti mismo! Controla las paletas usando las teclas 'W' y 'S' para el Jugador 1, e 'I' y 'K' para el Jugador 2.
- **Velocidad Dinámica de la Pelota:** La velocidad de la pelota aumenta gradualmente con el tiempo, proporcionando un desafío adicional a medida que avanza el juego.
- **Sistema de Puntuación:** Lleva el registro de la puntuación de cada jugador que se muestra en la pantalla. El juego reinicia automáticamente la pelota e incrementa la puntuación del jugador contrario cuando la pelota toca la pared izquierda o derecha sin ser interceptada por la paleta.
- **Agregar Bolas Adicionales:** Presiona la barra espaciadora para agregar más bolas al juego, aumentando la complejidad y emoción.
- **Pausar el juego:** Los usuarios tienen la capacidad de pausar el juego cuando lo deseen utilizando la tecla 'p'. Esto permite a los jugadores tomar un respiro o planificar su estrategia sin salir del juego.

## **Cómo Jugar:**
### 1. Instalación:
- Asegúrate de tener Python instalado en tu sistema.
- Clona este repositorio en tu máquina local.

### 2. Ejecutar el Juego:
- Abre una terminal o símbolo del sistema y navega hasta el directorio donde se encuentran los archivos del juego.
- Ejecuta el siguiente comando: python pong.py
- La ventana del juego se abrirá y podrás comenzar a jugar inmediatamente.

### 3. Controles del Juego:
- **Jugador 1:**
- Mover arriba: 'W'
- Mover abajo: 'S'
- **Jugador 2:**
- Mover arriba: 'I'
- Mover abajo: 'K'
- Agregar bolas adicionales: Presiona la barra espaciadora.
- Pausar el juego: Presiona la tecla 'p'.

### 4. Objetivo:
- Usa tu paleta para evitar que la pelota golpee las paredes detrás de ti.
- Rebota la pelota de regreso hacia el lado de tu oponente para marcar puntos.
- El juego termina cuando un jugador alcanza 10 puntos, determinando al ganador.

## **Cambios del juego original:**
- **Adición de un segundo jugador:** El juego originalmente estaba diseñado para ser jugado por un solo jugador contra la computadora. En esta versión modificada, se ha agregado la capacidad de jugar contra otro jugador humano, lo que agrega una dimensión competitiva y social al juego.
- **Velocidad dinámica de la pelota:** En el juego original, la velocidad de la pelota puede ser constante o predefinida. En esta versión modificada, la velocidad de la pelota aumenta gradualmente con el tiempo, lo que aumenta la dificultad y la emoción del juego a medida que avanza.
- **Sistema de puntuación:** Se ha agregado un sistema de puntuación para llevar un registro de los puntos obtenidos por cada jugador. Además, se ha implementado un mecanismo para reiniciar la pelota y actualizar la puntuación cuando la pelota toca la pared sin ser interceptada por la paleta del jugador.
- **Adición de bolas adicionales:** Se ha agregado la capacidad de agregar más bolas al juego presionando la barra espaciadora. Esto agrega una capa adicional de complejidad y desafío al juego, ya que los jugadores deben administrar múltiples bolas simultáneamente.
- **Interfaz gráfica mejorada:** Aunque el juego sigue utilizando el módulo Turtle de Python para la representación gráfica, se han realizado mejoras en la presentación visual y la legibilidad del juego, como la incorporación de colores y la adaptación de los elementos visuales a las pantallas modernas.
- **Pausar y reanudar el juego:** Añadida la capacidad de pausar y reanudar el juego, lo que ofrece a los jugadores mayor flexibilidad durante el juego. Pueden pausar el juego en cualquier momento presionando la tecla 'p', lo que es útil para tomar un descanso o discutir estrategias sin perder el progreso del juego.

**¡Disfruta del Juego!**

## **Reconocimientos:**
Este juego está basado en el clásico juego Pong creado originalmente por Atari.
Un agradecimiento especial al módulo Freegames por proporcionar funciones de utilidad.
Siéntete libre de contribuir al proyecto enviando correcciones de errores, nuevas características o sugerencias. ¡Diviértete jugando Pong!