"""
food.py
-------
Modelo del alimento.

Relación con el sílabo:
- Unidad 2: variables y tipos de datos (enteros, tuplas).
- Unidad 3: bucle while para generar posiciones válidas (estructura
  repetitiva controlada por condición).
- Unidad 4: función con parámetros y valor de retorno
  (generar_nueva_posicion), uso de listas/tuplas como estructura de datos.
"""

import random


class Food:
    def __init__(self, ancho_tablero, alto_tablero):
        self.ancho_tablero = ancho_tablero
        self.alto_tablero = alto_tablero
        self.position = (0, 0)  # Unidad 2: tupla (x, y)

    def generar_nueva_posicion(self, cuerpo_serpiente):
        """
        Genera una nueva posición aleatoria y válida para el alimento.

        Parámetro:
            cuerpo_serpiente (list): lista de tuplas ocupadas por la serpiente.
        Retorna:
            tuple: nueva posición (x, y) del alimento.

        Unidad 3: bucle while (estructura repetitiva) que se repite
        mientras la posición elegida no sea válida.
        """
        posicion_valida = False
        while not posicion_valida:
            x = random.randint(0, self.ancho_tablero - 1)
            y = random.randint(0, self.alto_tablero - 1)

            if (x, y) not in cuerpo_serpiente:
                posicion_valida = True
                self.position = (x, y)

        return self.position
