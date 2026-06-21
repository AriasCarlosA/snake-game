"""
main.py
-------
Punto de entrada del programa.
Crea una instancia de Game y ejecuta el bucle principal del juego.

Para ejecutar:
    python main.py
"""

from game import Game


def main():
    juego = Game()
    juego.ejecutar()


if __name__ == "__main__":
    main()
