"""
snake.py
--------
Modelo de la serpiente.

Relación con el sílabo de Lógica de Programación:
- Unidad 2 (Manejo de datos): atributos como variables tipadas (listas,
  tuplas, enteros) que representan el estado de la serpiente.
- Unidad 3 (Condicionales y bucles): validación de dirección con if,
  recorrido del cuerpo con for/while en los métodos de colisión.
- Unidad 4 (Estructuras de datos y funciones): el cuerpo de la serpiente
  se modela como una LISTA de TUPLAS (x, y); todos los métodos son
  funciones con parámetros y valores de retorno explícitos.
"""


class Snake:
    def __init__(self, x, y, tamano_celda):
        """
        Inicializa la serpiente con una sola celda (cabeza) en (x, y).

        Parámetros:
            x (int), y (int): coordenadas iniciales de la cabeza.
            tamano_celda (int): tamaño en píxeles de cada celda del tablero.
        """
        self.tamano_celda = tamano_celda

        # Unidad 4: el cuerpo se representa como una LISTA de TUPLAS (x, y).
        # El primer elemento siempre es la cabeza.
        self.body = [(x, y)]

        # Unidad 2: variable tupla que guarda la dirección actual (dx, dy).
        self.direction = (1, 0)

        # Unidad 2: variable booleana (tipo de dato básico) usada como bandera.
        self.crecer_pendiente = False

    def cambiar_direccion(self, nueva_direccion):
        """
        Cambia la dirección de movimiento.

        Parámetro:
            nueva_direccion (tuple): nueva dirección (dx, dy).
        Retorna:
            bool: True si el cambio fue aplicado, False si fue rechazado.

        Unidad 3: estructura condicional if/else para evitar que la
        serpiente se mueva en sentido contrario a sí misma.
        """
        dx, dy = nueva_direccion
        dx_actual, dy_actual = self.direction

        if (dx, dy) != (-dx_actual, -dy_actual):
            self.direction = nueva_direccion
            return True
        else:
            return False

    def mover(self):
        """
        Mueve la serpiente un paso en la dirección actual.
        Retorna la nueva posición de la cabeza (tupla).

        Unidad 4: manipulación de listas (insert/pop) para simular
        el desplazamiento del cuerpo.
        """
        cabeza_x, cabeza_y = self.body[0]
        dx, dy = self.direction

        nueva_cabeza = (cabeza_x + dx, cabeza_y + dy)
        self.body.insert(0, nueva_cabeza)

        # Unidad 3: condicional simple if/else
        if not self.crecer_pendiente:
            self.body.pop()
        else:
            self.crecer_pendiente = False

        return nueva_cabeza

    def crecer(self):
        """Marca que la serpiente debe crecer en el próximo movimiento."""
        self.crecer_pendiente = True

    def obtener_cabeza(self):
        """Retorna la posición actual de la cabeza (tupla x, y)."""
        return self.body[0]

    def obtener_longitud(self):
        """Retorna la cantidad de segmentos del cuerpo (función con retorno)."""
        return len(self.body)

    def colisiona_con_borde(self, ancho_tablero, alto_tablero):
        """
        Verifica colisión con los bordes del tablero.

        Parámetros: ancho_tablero (int), alto_tablero (int).
        Retorna: bool.

        Unidad 3: condicionales anidadas (if/or) para verificar límites.
        """
        x, y = self.obtener_cabeza()
        if x < 0 or x >= ancho_tablero or y < 0 or y >= alto_tablero:
            return True
        return False

    def colisiona_con_cuerpo(self):
        """
        Verifica si la cabeza choca con algún segmento del propio cuerpo.

        Unidad 3/4: recorrido (búsqueda) sobre una lista mediante el
        operador `in`, equivalente a un bucle for de búsqueda.
        """
        cabeza = self.obtener_cabeza()
        resto_cuerpo = self.body[1:]  # Unidad 4: slicing de listas
        for segmento in resto_cuerpo:  # Unidad 3: bucle for explícito
            if segmento == cabeza:
                return True
        return False
