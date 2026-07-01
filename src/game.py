"""
game.py
-------
Clase Game: coordina todos los componentes del juego (bucle principal,
entradas del jugador, colisiones, puntuación y dibujo en pantalla).

Corresponde a la Capa de Lógica (Controlador) y, de forma simplificada,
también a la Capa de Presentación (Vista) dentro de la arquitectura MVC.

Relación con el sílabo:
- Unidad 1: el método ejecutar() representa el algoritmo / bucle
  principal que resuelve el problema del juego paso a paso.
- Unidad 2: variables y tipos de datos básicos (enteros, booleanos,
  cadenas) y un DICCIONARIO (CONFIG) para parámetros del juego.
- Unidad 3: condicionales (if/elif/else) para procesar teclas y bucles
  (while en ejecutar(), for al dibujar el cuerpo).
- Unidad 4: diccionarios (CONFIG, TECLAS_DIRECCION), listas (body) y
  funciones con parámetros y retorno (calcular_puntuacion, etc.).
"""

import pygame
import sys

from snake import Snake
from food import Food

# Unidad 4 / Unidad 2: DICCIONARIO con la configuración general del juego.
# Usar un diccionario centraliza los "tipos de datos básicos" del juego
# (enteros, tuplas de color) bajo claves legibles.
CONFIG = {
    "tamano_celda": 20,
    "columnas": 30,
    "filas": 20,
    "fps": 10,  # Cumple el requisito no funcional de 10 fps mínimo
}

# Unidad 4: diccionario de colores (clave: nombre, valor: tupla RGB)
COLORES = {
    "fondo": (0, 0, 0),
    "serpiente": (0, 200, 0),
    "alimento": (200, 0, 0),
    "texto": (255, 255, 255),
}

# Unidad 4: diccionario que asocia cada tecla con una dirección (tupla).
# Reemplaza una larga cadena de if/elif por una búsqueda en diccionario.
TECLAS_DIRECCION = {
    pygame.K_UP: (0, -1),
    pygame.K_DOWN: (0, 1),
    pygame.K_LEFT: (-1, 0),
    pygame.K_RIGHT: (1, 0),
}


def calcular_puntuacion(alimentos_comidos, puntos_por_alimento=1):
    """
    Función con parámetros y valor de retorno (Unidad 4).

    Parámetros:
        alimentos_comidos (int): cantidad de alimentos consumidos.
        puntos_por_alimento (int): puntos otorgados por cada alimento.
    Retorna:
        int: puntuación total.
    """
    return alimentos_comidos * puntos_por_alimento


def formatear_texto_puntuacion(puntuacion):
    """
    Función con parámetro y retorno: arma el texto a mostrar en pantalla.

    Parámetro:
        puntuacion (int)
    Retorna:
        str
    """
    return f"Puntuacion: {puntuacion}"


class Game:
    # Constantes derivadas del diccionario CONFIG (Unidad 2: variables)
    TAMANO_CELDA = CONFIG["tamano_celda"]
    COLUMNAS = CONFIG["columnas"]
    FILAS = CONFIG["filas"]
    ANCHO_PANTALLA = COLUMNAS * TAMANO_CELDA
    ALTO_PANTALLA = FILAS * TAMANO_CELDA
    FPS = CONFIG["fps"]

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

        # Unidad 2: variables con tipos de datos básicos
        self.alimentos_comidos = 0  # int
        self.puntuacion = 0         # int
        self.juego_terminado = False  # bool

    def procesar_eventos(self):
        """
        Captura y procesa las entradas del teclado del jugador.

        Unidad 3 / Unidad 4: en lugar de una cadena larga de if/elif,
        se usa el diccionario TECLAS_DIRECCION para resolver la
        dirección asociada a la tecla presionada.
        """
        for evento in pygame.event.get():  # Unidad 3: bucle for
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key in TECLAS_DIRECCION:
                    direccion = TECLAS_DIRECCION[evento.key]
                    self.snake.cambiar_direccion(direccion)
                elif evento.key == pygame.K_r and self.juego_terminado:
                    self.reiniciar_juego()

    def actualizar(self):
        """
        Actualiza el estado del juego: mueve la serpiente, verifica
        colisión con el alimento y con bordes/cuerpo propio.
        """
        if self.juego_terminado:
            return

        self.snake.mover()

        if self.snake.obtener_cabeza() == self.food.position:
            self.snake.crecer()
            self.alimentos_comidos += 1
            self.puntuacion = calcular_puntuacion(self.alimentos_comidos)
            self.food.generar_nueva_posicion(self.snake.body)

        if self.snake.colisiona_con_borde(self.COLUMNAS, self.FILAS):
            self.juego_terminado = True

        if self.snake.colisiona_con_cuerpo():
            self.juego_terminado = True

    def dibujar(self):
        """
        Dibuja todos los elementos del juego en pantalla: tablero,
        serpiente, alimento y puntuación.
        """
        self.pantalla.fill(COLORES["fondo"])

        # Unidad 3: bucle for que recorre la LISTA de tuplas del cuerpo
        for segmento in self.snake.body:
            x, y = segmento
            rect = pygame.Rect(
                x * self.TAMANO_CELDA,
                y * self.TAMANO_CELDA,
                self.TAMANO_CELDA,
                self.TAMANO_CELDA,
            )
            pygame.draw.rect(self.pantalla, COLORES["serpiente"], rect)

        fx, fy = self.food.position
        rect_alimento = pygame.Rect(
            fx * self.TAMANO_CELDA,
            fy * self.TAMANO_CELDA,
            self.TAMANO_CELDA,
            self.TAMANO_CELDA,
        )
        pygame.draw.rect(self.pantalla, COLORES["alimento"], rect_alimento)

        texto_puntuacion = self.fuente.render(
            formatear_texto_puntuacion(self.puntuacion), True, COLORES["texto"]
        )
        self.pantalla.blit(texto_puntuacion, (10, 10))

        if self.juego_terminado:
            texto_fin = self.fuente.render(
                "Juego terminado - Presiona R para reiniciar",
                True,
                COLORES["texto"],
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

        Unidad 1 / Unidad 3: estructura repetitiva while True que
        representa el algoritmo central de resolución del problema:
        leer entrada -> actualizar estado -> dibujar -> repetir.
        """
        while True:
            self.procesar_eventos()
            self.actualizar()
            self.dibujar()
            self.reloj.tick(self.FPS)
