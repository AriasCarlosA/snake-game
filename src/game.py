"""
game.py
-------
Clase Game: coordina todos los componentes del juego.
Gestiona el bucle principal (game loop), procesa las entradas
del jugador, verifica colisiones, actualiza la puntuación
y dibuja todo en pantalla.

Corresponde a la Capa de Lógica (Controlador) y, de forma
simplificada, también a la Capa de Presentación (Vista)
dentro de la arquitectura MVC descrita en el documento.
"""

import pygame
import sys

from snake import Snake
from food import Food


class Game:
    # Constantes de configuración del juego
    TAMANO_CELDA = 20
    COLUMNAS = 30
    FILAS = 20
    ANCHO_PANTALLA = COLUMNAS * TAMANO_CELDA
    ALTO_PANTALLA = FILAS * TAMANO_CELDA
    FPS = 10  # Cumple con el requisito no funcional de 10 fps mínimo

    # Colores (R, G, B)
    COLOR_FONDO = (0, 0, 0)
    COLOR_SERPIENTE = (0, 200, 0)
    COLOR_ALIMENTO = (200, 0, 0)
    COLOR_TEXTO = (255, 255, 255)

    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode(
            (self.ANCHO_PANTALLA, self.ALTO_PANTALLA)
        )
        pygame.display.set_caption("Juego de la Serpiente - UIDE")
        self.reloj = pygame.time.Clock()
        self.fuente = pygame.font.SysFont("Arial", 22)

        self.reiniciar_juego()

    def reiniciar_juego(self):
        """Inicializa o reinicia el estado del juego."""
        centro_x = self.COLUMNAS // 2
        centro_y = self.FILAS // 2

        self.snake = Snake(centro_x, centro_y, self.TAMANO_CELDA)
        self.food = Food(self.COLUMNAS, self.FILAS)
        self.food.generar_nueva_posicion(self.snake.body)

        self.puntuacion = 0
        self.juego_terminado = False

    def procesar_eventos(self):
        """
        Captura y procesa las entradas del teclado del jugador.
        Corresponde al módulo InputHandler del diagrama de clases.
        """
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                # Estructura condicional: según la tecla presionada,
                # cambiamos la dirección de la serpiente.
                if evento.key == pygame.K_UP:
                    self.snake.cambiar_direccion((0, -1))
                elif evento.key == pygame.K_DOWN:
                    self.snake.cambiar_direccion((0, 1))
                elif evento.key == pygame.K_LEFT:
                    self.snake.cambiar_direccion((-1, 0))
                elif evento.key == pygame.K_RIGHT:
                    self.snake.cambiar_direccion((1, 0))
                elif evento.key == pygame.K_r and self.juego_terminado:
                    # Permite reiniciar el juego al presionar "R"
                    self.reiniciar_juego()

    def actualizar(self):
        """
        Actualiza el estado del juego: mueve la serpiente,
        verifica colisión con el alimento y con bordes/cuerpo.
        """
        # Si el juego ya terminó, no actualizamos nada más
        if self.juego_terminado:
            return

        self.snake.mover()

        # Verificar colisión con el alimento
        if self.snake.obtener_cabeza() == self.food.position:
            self.snake.crecer()
            self.puntuacion += 1
            self.food.generar_nueva_posicion(self.snake.body)

        # Verificar colisión con los bordes del tablero
        if self.snake.colisiona_con_borde(self.COLUMNAS, self.FILAS):
            self.juego_terminado = True

        # Verificar colisión con el propio cuerpo
        if self.snake.colisiona_con_cuerpo():
            self.juego_terminado = True

    def dibujar(self):
        """
        Dibuja todos los elementos del juego en pantalla:
        tablero, serpiente, alimento y puntuación.
        Corresponde al módulo Renderer del diagrama de clases.
        """
        self.pantalla.fill(self.COLOR_FONDO)

        # Dibujar la serpiente: recorremos cada segmento del cuerpo
        for segmento in self.snake.body:
            x, y = segmento
            rect = pygame.Rect(
                x * self.TAMANO_CELDA,
                y * self.TAMANO_CELDA,
                self.TAMANO_CELDA,
                self.TAMANO_CELDA,
            )
            pygame.draw.rect(self.pantalla, self.COLOR_SERPIENTE, rect)

        # Dibujar el alimento
        fx, fy = self.food.position
        rect_alimento = pygame.Rect(
            fx * self.TAMANO_CELDA,
            fy * self.TAMANO_CELDA,
            self.TAMANO_CELDA,
            self.TAMANO_CELDA,
        )
        pygame.draw.rect(self.pantalla, self.COLOR_ALIMENTO, rect_alimento)

        # Mostrar la puntuación actual
        texto_puntuacion = self.fuente.render(
            f"Puntuacion: {self.puntuacion}", True, self.COLOR_TEXTO
        )
        self.pantalla.blit(texto_puntuacion, (10, 10))

        # Si el juego terminó, mostramos mensaje final
        if self.juego_terminado:
            texto_fin = self.fuente.render(
                "Juego terminado - Presiona R para reiniciar",
                True,
                self.COLOR_TEXTO,
            )
            self.pantalla.blit(
                texto_fin,
                (
                    self.ANCHO_PANTALLA // 2 - texto_fin.get_width() // 2,
                    self.ALTO_PANTALLA // 2,
                ),
            )

        pygame.display.flip()

    def ejecutar(self):
        """
        Bucle principal del juego (game loop).
        Se repite continuamente hasta que el jugador cierra la ventana.
        """
        while True:
            self.procesar_eventos()
            self.actualizar()
            self.dibujar()
            self.reloj.tick(self.FPS)
