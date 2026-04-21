import sys
import os

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

theta0_deg = 88
theta0 = np.deg2rad(theta0_deg) # Este valor es solo el punto de partida
omega0 = 0.0

T = 12
dt = 0.01
t = np.arange(0, T, dt)

k = 3 * g / (2 * L)

# =========================================================
# DINÁMICAS
# =========================================================
def nonlinear(t, y):
    theta, omega = y
    return np.array([omega, -k * np.sin(theta)])

def linear(t, y):
    theta, omega = y
    return np.array([omega, -k * theta])

# =========================================================
# SIMULACIONES
# =========================================================
y0 = np.array([theta0, omega0])

sol_nl = simulate(nonlinear, y0, t)
sol_li = simulate(linear, y0, t)

theta_nl = sol_nl[:, 0]
theta_li = sol_li[:, 0]

# =========================================================
# FIGURA
# =========================================================
fig = plt.figure(figsize=(12, 5))

# Panel izquierdo: animación
ax1 = fig.add_subplot(1, 2, 1)
ax1.set_aspect('equal')
ax1.set_xlim(-1.2 * L, 1.2 * L)
ax1.set_ylim(-1.2 * L, 1.2 * L)
ax1.set_title("Nonlinear vs Linear")
ax1.grid()

line_nl, = ax1.plot([], [], 'o-', lw=3, label='Nonlinear')
line_li, = ax1.plot([], [], 'o--', lw=2, label='Linear')
ax1.legend()

# Panel derecho: theta(t)
ax2 = fig.add_subplot(1, 2, 2)
ax2.set_title("θ(t)")
ax2.set_xlabel("Time [s]")
ax2.set_ylabel("θ [rad]")
ax2.grid()

ax2.set_xlim(t[0], t[-1])

theta_min = min(theta_nl.min(), theta_li.min())
theta_max = max(theta_nl.max(), theta_li.max())
margin = 0.1 * (theta_max - theta_min if theta_max != theta_min else 1.0)
ax2.set_ylim(theta_min - margin, theta_max + margin)

trace_nl, = ax2.plot([], [], lw=2, label='Nonlinear')
trace_li, = ax2.plot([], [], '--', lw=2, label='Linear')
ax2.legend()
ax2.set_title(f"Evolución angular θ(t), condición inicial θ₀ = {theta0_deg}°")

# =========================================================
# UPDATE
# =========================================================
def update(frame):
    th_nl = theta_nl[frame]
    th_li = theta_li[frame]

    x_nl = L * np.sin(th_nl)
    y_nl = -L * np.cos(th_nl)

    x_li = L * np.sin(th_li)
    y_li = -L * np.cos(th_li)

    line_nl.set_data([0, x_nl], [0, y_nl])
    line_li.set_data([0, x_li], [0, y_li])

    trace_nl.set_data(t[:frame+1], theta_nl[:frame+1])
    trace_li.set_data(t[:frame+1], theta_li[:frame+1])

    return line_nl, line_li, trace_nl, trace_li

ani = FuncAnimation(fig, update, frames=len(t), interval=20, repeat=True)

plt.tight_layout()
plt.show()