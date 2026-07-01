# 🐍 Juego de la Serpiente (Snake Game)

Proyecto Integrador para el curso de **Lógica de Programación** — Universidad Internacional del Ecuador (UIDE).

**Autor:** Carlos Arias
**Profesora:** Estefanía Vanessa Heredia Jiménez

## 📋 Descripción

Implementación en **Python** (con la librería `pygame`) del clásico juego de la serpiente. El jugador controla una serpiente que se mueve por un tablero, debe comer alimentos para crecer y ganar puntos, y pierde si choca contra los bordes del tablero o contra su propio cuerpo.

El proyecto integra de forma explícita el contenido de las 4 unidades del sílabo de Lógica de Programación:

| Unidad | Tema | Dónde se aplica |
|--------|------|------------------|
| 1 | Resolución de problemas y entorno de programación | Algoritmo general del juego (`main.py`, bucle `ejecutar()` en `game.py`) |
| 2 | Variables y tipos de datos básicos | Enteros, booleanos, cadenas y tuplas en `snake.py`, `food.py`, `game.py` |
| 3 | Condicionales (`if/elif/else`) y bucles (`while`, `for`) | Validación de dirección, detección de colisiones, bucle principal del juego |
| 4 | Estructuras de datos (listas, tuplas, diccionarios) y funciones | Cuerpo de la serpiente como lista de tuplas, diccionarios `CONFIG`/`COLORES`/`TECLAS_DIRECCION`, funciones con parámetros y retorno |

El diseño sigue el patrón de arquitectura **Modelo-Vista-Controlador (MVC)**, separando la lógica del juego, el estado de los datos y la representación visual.

## 🎮 Cómo jugar

- Usa las flechas del teclado (`↑` `↓` `←` `→`) para controlar la dirección de la serpiente.
- Come los cuadros rojos (alimento) para crecer y aumentar tu puntuación.
- Evita chocar contra los bordes del tablero o contra el cuerpo de la serpiente.
- Cuando el juego termine, presiona `R` para reiniciar.

## 🛠️ Requisitos

- Python 3.8 o superior
- Librería `pygame`

## ⚙️ Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/AriasCarlosA/snake-game.git
   cd snake-game
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Ejecución

```bash
cd src
python main.py
```

## 📂 Estructura del proyecto

```
snake-game/
│
├── diagramas/                     # Diagramas de diseño del sistema
│   ├── diagrama_flujo.png
│   ├── diagrama_casos_uso.png
│   └── diagrama_arquitectura.png
│
├── src/                            # Código fuente del juego
│   ├── main.py                     # Punto de entrada del programa
│   ├── snake.py                    # Clase Snake (modelo de la serpiente)
│   ├── food.py                     # Clase Food (modelo del alimento)
│   └── game.py                     # Clase Game (controlador y vista)
│
├── requirements.txt
└── README.md
```

## 🧩 Arquitectura del sistema

El proyecto sigue el patrón **MVC**:

| Capa | Componente | Responsabilidad |
|------|------------|------------------|
| Modelo | `Snake`, `Food` | Mantienen el estado del juego (posición, dirección, alimento) |
| Controlador | `Game` (lógica) | Gestiona el bucle principal, procesa entradas y reglas del juego |
| Vista | `Game` (renderizado) | Dibuja el tablero, la serpiente, el alimento y la puntuación |

Adicionalmente se identifican dos módulos de apoyo:
- **Módulo de Detección de Colisiones**: verifica choques con bordes y con el propio cuerpo.
- **Módulo de Generación Aleatoria**: genera posiciones válidas para el alimento.

## 📊 Diagramas

En la carpeta [`diagramas/`](./diagramas) se encuentran:

- **Diagrama de Flujo**: describe el ciclo de vida de una partida (inicio → bucle principal → fin).
- **Diagrama de Casos de Uso**: muestra las interacciones entre el Jugador y el Sistema de Juego.
- **Diagrama de Arquitectura**: representa la organización del sistema según el patrón MVC.

## ✅ Requisitos funcionales cubiertos

- [x] Control de dirección mediante teclas
- [x] Movimiento continuo de la serpiente
- [x] Generación aleatoria de alimentos en posiciones válidas
- [x] Crecimiento de la serpiente al comer
- [x] Detección de colisiones (bordes y cuerpo propio)
- [x] Visualización de la puntuación actual
- [x] Fin de partida con puntuación final
- [x] Reinicio del juego

## 📚 Referencias

- Bass, L., Clements, P., & Kazman, R. (2021). *Software architecture in practice* (4th ed.). Addison-Wesley Professional.
- Fowler, M. (2018). *UML distilled: A brief guide to the standard object modeling language* (3rd ed.). Addison-Wesley Professional.
- Pressman, R. S., & Maxim, B. R. (2020). *Software engineering: A practitioner's approach* (9th ed.). McGraw-Hill Education.
- Sommerville, I. (2022). *Software engineering* (10th ed.). Pearson Education.
