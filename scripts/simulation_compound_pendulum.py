import sys
import os

# Agrega la carpeta raíz del proyecto al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from utils.integrators import simulate

# =========================================================
# PARÁMETROS
# =========================================================
g = 9.81
L = 1.0

theta0_deg = 60
theta0 = np.deg2rad(theta0_deg)
omega0 = 0.0

T = 10
dt = 0.01
t = np.arange(0, T, dt)

# =========================================================
# DINÁMICA (NO LINEAL)
# =========================================================
def dynamics(t, y):
    theta, omega = y

    dtheta = omega
    domega = -(3 * g / (2 * L)) * np.sin(theta)

    return np.array([dtheta, domega])

# =========================================================
# SIMULACIÓN
# =========================================================
y0 = np.array([theta0, omega0])
sol = simulate(dynamics, y0, t)

theta = sol[:, 0]

# =========================================================
# ANIMACIÓN
# =========================================================
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-1.2 * L, 1.2 * L)
ax.set_ylim(-1.2 * L, 1.2 * L)
ax.set_title("Compound Pendulum (Nonlinear Model)")
ax.grid()

line, = ax.plot([], [], 'o-', lw=3)
pivot, = ax.plot(0, 0, 'ko')

text = ax.text(-1.1, 1.0, '')

def update(frame):
    th = theta[frame]

    x = L * np.sin(th)
    y = -L * np.cos(th)

    line.set_data([0, x], [0, y])

    text.set_text(f"theta0 = {theta0_deg} deg\nt = {t[frame]:.2f} s")

    return line, text

ani = FuncAnimation(fig, update, frames=len(t), interval=20)

plt.show()