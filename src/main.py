"""
main.py
-------
Punto de entrada del programa. Crea una instancia de Game y ejecuta
el bucle principal del juego.

Unidad 1 (Resolución de problemas y entorno de programación):
este módulo representa el punto de partida del algoritmo general
que resuelve el problema planteado (jugar Snake).

Para ejecutar:
    python main.py
"""

from game import Game


def main():
    """Función principal sin parámetros que arranca el juego."""
    juego = Game()
    juego.ejecutar()


if __name__ == "__main__":
    main()
