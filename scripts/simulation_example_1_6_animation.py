import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from utils.integrators import simulate
from utils.example_1_6_dynamics import get_default_params, dynamics


# =========================================================
# PARÁMETROS
# =========================================================
params = get_default_params()

params["m"] = 1.0
params["L1"] = 1.0
params["L2"] = 1.2
params["g"] = 9.81
params["F"] = 0.0   # puedes probar luego con F != 0

L1 = params["L1"]
L2 = params["L2"]

# =========================================================
# CONDICIONES INICIALES
# =========================================================
theta1_0_deg = 5
theta2_0_deg = 36.0

theta1_0 = np.deg2rad(theta1_0_deg)
theta2_0 = np.deg2rad(theta2_0_deg)

omega1_0 = 0.0
omega2_0 = 0.0

y0 = np.array([theta1_0, theta2_0, omega1_0, omega2_0], dtype=float)

# =========================================================
# TIEMPO DE SIMULACIÓN
# =========================================================
T = 10.0
dt = 0.001
t = np.arange(0.0, T + dt, dt)

# =========================================================
# FUNCIÓN DINÁMICA ENVUELTA
# =========================================================
def f(ti, yi):
    return dynamics(ti, yi, params)

# =========================================================
# SIMULACIÓN
# =========================================================
sol = simulate(f, y0, t)

theta1 = sol[:, 0]
theta2 = sol[:, 1]

# =========================================================
# GEOMETRÍA DEL SISTEMA
# =========================================================
# Sistema de referencia:
# O = punto fijo en (0,0)
# La cuerda forma ángulo theta1 respecto de la vertical
# La barra forma ángulo theta2 respecto de la vertical
#
# Entonces:
# A = extremo inferior de la cuerda
# B = extremo libre de la barra
# C = centro de masa de la barra

def compute_positions(th1, th2, L1, L2):
    # Punto O
    xO, yO = 0.0, 0.0

    # Punto A (extremo de la cuerda)
    xA = L1 * np.sin(th1)
    yA = -L1 * np.cos(th1)

    # Punto B (extremo libre de la barra)
    xB = xA + L2 * np.sin(th2)
    yB = yA - L2 * np.cos(th2)

    # Centro de masa C
    xC = xA + (L2 / 2.0) * np.sin(th2)
    yC = yA - (L2 / 2.0) * np.cos(th2)

    return (xO, yO), (xA, yA), (xB, yB), (xC, yC)

# =========================================================
# FIGURA
# =========================================================
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')
ax.grid(True)

reach = L1 + L2 + 0.3
ax.set_xlim(-reach, reach)
ax.set_ylim(-reach, 0.5)
ax.set_title('Example 1.6 — Animación del sistema')
ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.set_title(
    f"Example 1.6 — θ1={theta1_0_deg}°, θ2={theta2_0_deg}°"
)

# Elementos gráficos
string_line, = ax.plot([], [], 'o-', lw=3, label='Cuerda')
bar_line, = ax.plot([], [], 'o-', lw=4, label='Barra')
cm_point, = ax.plot([], [], 'ro', markersize=8, label='Centro de masa C')
pivot_point, = ax.plot(0, 0, 'ko', markersize=8, label='Pivote O')

time_text = ax.text(
    0.02, 0.95, '', transform=ax.transAxes, fontsize=11, verticalalignment='top'
)

angles_text = ax.text(
    0.02, 0.87, '', transform=ax.transAxes, fontsize=11, verticalalignment='top'
)

ax.legend(loc='upper right')

# =========================================================
# UPDATE
# =========================================================
def update(frame):
    th1 = theta1[frame]
    th2 = theta2[frame]

    O, A, B, C = compute_positions(th1, th2, L1, L2)

    # cuerda O-A
    string_line.set_data([O[0], A[0]], [O[1], A[1]])

    # barra A-B
    bar_line.set_data([A[0], B[0]], [A[1], B[1]])

    # centro de masa C
    cm_point.set_data([C[0]], [C[1]])

    time_text.set_text(f't = {t[frame]:.2f} s')
    angles_text.set_text(
        f'θ1 = {np.rad2deg(th1):.2f}°\n'
        f'θ2 = {np.rad2deg(th2):.2f}°'
    )

    return string_line, bar_line, cm_point, time_text, angles_text

ani = FuncAnimation(
    fig,
    update,
    frames=len(t),
    interval=20,
    repeat=True
)

plt.tight_layout()
plt.show()