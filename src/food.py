"""
food.py
-------
Clase Food: representa el alimento que la serpiente debe comer.
Genera posiciones aleatorias válidas (que no estén ocupadas
por el cuerpo de la serpiente).

Corresponde a la clase "Food" del Diagrama de Clases y al
"Módulo de Generación Aleatoria" de la arquitectura del sistema.
"""

import random


class Food:
    def __init__(self, ancho_tablero, alto_tablero):
        self.ancho_tablero = ancho_tablero
        self.alto_tablero = alto_tablero
        self.position = (0, 0)

    def generar_nueva_posicion(self, cuerpo_serpiente):
        """
        Genera una nueva posición aleatoria para el alimento,
        asegurándose de que no caiga sobre el cuerpo de la serpiente.
        """
        while True:
            x = random.randint(0, self.ancho_tablero - 1)
            y = random.randint(0, self.alto_tablero - 1)

            # Condicional: si la posición elegida no está ocupada
            # por la serpiente, es válida y salimos del bucle.
            if (x, y) not in cuerpo_serpiente:
                self.position = (x, y)
                break

        return self.position
