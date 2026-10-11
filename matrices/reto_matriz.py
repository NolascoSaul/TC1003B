import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ------------------------------------------------------------
# Utilidades de transformacion 2D con matrices homogeneas (3x3)
# ------------------------------------------------------------

def T(tx, ty):
    """Matriz de traslacion"""
    return np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ], dtype=float)


def R(theta):
    """Matriz de rotacion"""
    c, s = np.cos(theta), np.sin(theta)
    return np.array([
        [c, -s, 0],
        [s,  c, 0],
        [0,  0, 1]
    ], dtype=float)


def S(sx, sy):
    """Matriz de escalamiento"""
    return np.array([
        [sx, 0,  0],
        [0, sy,  0],
        [0,  0,  1]
    ], dtype=float)


def aplicar(A, M):
    """Aplica transformacion A a la matriz de puntos M (3 x n)."""
    return A @ M


def puntos_homogeneos(pts2d):
    """Convierte lista de puntos 2D en matriz 3 x n"""
    arr = np.array(pts2d, dtype=float).T
    ones = np.ones((1, arr.shape[1]))
    return np.vstack((arr, ones))


# ------------------------------------------------------------
# Partes del dibujo base (cohete caricatura)
# ------------------------------------------------------------
# Cada parte es un poligono definido en coordenadas locales

partes_base = [
    {
        "nombre": "cuerpo",
        "color": "#f94144",
        "M": puntos_homogeneos([
            (-0.50, -1.10),
            ( 0.50, -1.10),
            ( 0.55,  0.50),
            ( 0.00,  1.20),
            (-0.55,  0.50),
            (-0.50, -1.10)
        ])
    },
    {
        "nombre": "ventana",
        "color": "#90e0ef",
        "M": puntos_homogeneos([
            (-0.18,  0.10),
            ( 0.18,  0.10),
            ( 0.18,  0.46),
            (-0.18,  0.46),
            (-0.18,  0.10)
        ])
    },
    {
        "nombre": "aleta_izq",
        "color": "#f3722c",
        "M": puntos_homogeneos([
            (-0.50, -0.90),
            (-1.00, -1.20),
            (-0.45, -0.30),
            (-0.50, -0.90)
        ])
    },
    {
        "nombre": "aleta_der",
        "color": "#f3722c",
        "M": puntos_homogeneos([
            ( 0.50, -0.90),
            ( 1.00, -1.20),
            ( 0.45, -0.30),
            ( 0.50, -0.90)
        ])
    },
    {
        "nombre": "llama",
        "color": "#f9c74f",
        "M": puntos_homogeneos([
            (-0.20, -1.10),
            ( 0.20, -1.10),
            ( 0.00, -1.75),
            (-0.20, -1.10)
        ])
    },
    {
        "nombre": "sonrisa",
        "color": "#14213d",
        "M": puntos_homogeneos([
            (-0.20, -0.05),
            (-0.10, -0.12),
            ( 0.00, -0.16),
            ( 0.10, -0.12),
            ( 0.20, -0.05)
        ])
    },
    {
        "nombre": "ojo_izq",
        "color": "#14213d",
        "M": puntos_homogeneos([
            (-0.13, 0.02),
            (-0.06, 0.02)
        ])
    },
    {
        "nombre": "ojo_der",
        "color": "#14213d",
        "M": puntos_homogeneos([
            ( 0.06, 0.02),
            ( 0.13, 0.02)
        ])
    }
]

# Estrellitas decorativas en el fondo
estrellas = [
    puntos_homogeneos([(-2.8, 1.8), (-2.7, 1.9), (-2.6, 1.8), (-2.7, 1.7), (-2.8, 1.8)]),
    puntos_homogeneos([( 2.5, 1.7), ( 2.65, 1.82), ( 2.8, 1.7), ( 2.65, 1.58), ( 2.5, 1.7)]),
    puntos_homogeneos([(-2.3,-1.7), (-2.18,-1.55), (-2.05,-1.7), (-2.18,-1.85), (-2.3,-1.7)]),
    puntos_homogeneos([( 2.2,-1.6), ( 2.35,-1.45), ( 2.5,-1.6), ( 2.35,-1.75), ( 2.2,-1.6)])
]


def dibujar_cohete(ax, angulo=0.0, escala=1.0, traslacion=(0.0, 0.0)):
    """Dibuja el cohete con una transformacion global."""
    ax.clear()

    # Fondo oscuro tipo espacio
    ax.set_facecolor("#0b132b")

    # Transformacion global: primero escala, luego rota, luego traslada
    A_global = T(traslacion[0], traslacion[1]) @ R(angulo) @ S(escala, escala)

    # Dibujar estrellas (sin rotar, solo de adorno)
    for est in estrellas:
        E = aplicar(np.eye(3), est)
        ax.plot(E[0], E[1], color="#e0fbfc", linewidth=1.2)

    # Dibujar cada parte transformada por matrices
    for p in partes_base:
        W = aplicar(A_global, p["M"])

        if p["nombre"] in ["ojo_izq", "ojo_der"]:
            ax.plot(W[0], W[1], "o", color=p["color"], markersize=5)
        elif p["nombre"] == "sonrisa":
            ax.plot(W[0], W[1], color=p["color"], linewidth=2)
        else:
            ax.fill(W[0], W[1], color=p["color"], alpha=0.95, edgecolor="#1b1b1b", linewidth=1.2)

    ax.set_xlim(-3.2, 3.2)
    ax.set_ylim(-2.6, 2.6)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("Cohete matricial: transformaciones lineales + traslacion", color="#e0fbfc")


# ------------------------------------------------------------
# Modo estatico o animado
# ------------------------------------------------------------
ANIMAR = True  # Cambia a False para mostrar una sola figura

fig, ax = plt.subplots(figsize=(7, 7))

if not ANIMAR:
    # Ejemplo estatico: rotado 25 grados y ligeramente escalado
    dibujar_cohete(ax, angulo=np.deg2rad(25), escala=1.15, traslacion=(0.0, 0.0))
    plt.show()
else:
    # Animacion: rota continuamente y "respira" en escala
    def update(frame):
        theta = np.deg2rad(frame)
        esc = 1.0 + 0.08 * np.sin(np.deg2rad(frame * 3))
        y = 0.12 * np.sin(np.deg2rad(frame * 2))
        dibujar_cohete(ax, angulo=theta, escala=esc, traslacion=(0.0, y))

    ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=35, repeat=True)
    plt.show()
