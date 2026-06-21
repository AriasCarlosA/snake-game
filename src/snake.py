"""
snake.py
--------
Clase Snake: representa el modelo de la serpiente.
Guarda las coordenadas del cuerpo, la dirección actual,
y tiene métodos para moverse y crecer.

Corresponde a la clase "Snake" del Diagrama de Clases
(Capa de Datos / Modelo en la arquitectura MVC).
"""


class Snake:
    def __init__(self, x, y, tamano_celda):
        """
        Inicializa la serpiente con una sola celda (cabeza)
        en la posición (x, y) y dirección inicial hacia la derecha.
        """
        self.tamano_celda = tamano_celda
        # El cuerpo es una lista de posiciones (x, y).
        # El primer elemento siempre es la cabeza.
        self.body = [(x, y)]
        # Dirección actual: (dx, dy). Empieza moviéndose a la derecha.
        self.direction = (1, 0)
        # Bandera para saber si debe crecer en el siguiente movimiento
        self.crecer_pendiente = False

    def cambiar_direccion(self, nueva_direccion):
        """
        Cambia la dirección de movimiento, evitando que la serpiente
        se mueva en sentido contrario a sí misma (lo que causaría
        una colisión inmediata con su propio cuerpo).
        """
        dx, dy = nueva_direccion
        dx_actual, dy_actual = self.direction

        # Condicional: no permitir invertir la dirección 180 grados
        if (dx, dy) != (-dx_actual, -dy_actual):
            self.direction = nueva_direccion

    def mover(self):
        """
        Mueve la serpiente en la dirección actual.
        Si hay un crecimiento pendiente (porque comió alimento),
        no se elimina la última celda, por lo que la serpiente crece.
        """
        cabeza_x, cabeza_y = self.body[0]
        dx, dy = self.direction

        # Nueva posición de la cabeza
        nueva_cabeza = (cabeza_x + dx, cabeza_y + dy)

        # Insertamos la nueva cabeza al inicio de la lista
        self.body.insert(0, nueva_cabeza)

        # Condicional: si no debe crecer, eliminamos la cola (último segmento)
        if not self.crecer_pendiente:
            self.body.pop()
        else:
            # Ya creció en este movimiento, reseteamos la bandera
            self.crecer_pendiente = False

    def crecer(self):
        """
        Marca que la serpiente debe crecer en el próximo movimiento.
        Se llama cuando la serpiente come un alimento.
        """
        self.crecer_pendiente = True

    def obtener_cabeza(self):
        """Devuelve la posición actual de la cabeza."""
        return self.body[0]

    def colisiona_con_borde(self, ancho_tablero, alto_tablero):
        """
        Verifica si la cabeza de la serpiente choca con los bordes
        del tablero de juego.
        """
        x, y = self.obtener_cabeza()
        if x < 0 or x >= ancho_tablero or y < 0 or y >= alto_tablero:
            return True
        return False

    def colisiona_con_cuerpo(self):
        """
        Verifica si la cabeza de la serpiente choca con su propio
        cuerpo (cualquier otro segmento del cuerpo).
        """
        cabeza = self.obtener_cabeza()
        # El resto del cuerpo es self.body[1:] (todo excepto la cabeza)
        return cabeza in self.body[1:]
