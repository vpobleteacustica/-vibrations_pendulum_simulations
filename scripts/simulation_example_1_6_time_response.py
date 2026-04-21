import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
import matplotlib.pyplot as plt

from utils.integrators import simulate
from utils.example_1_6_dynamics import get_default_params, dynamics


# =========================================================
# PARÁMETROS
# =========================================================
params = get_default_params()

# Puedes modificar estos valores para explorar
params["m"] = 1.0
params["L1"] = 1.0
params["L2"] = 1.2
params["g"] = 9.81
params["F"] = 0.0   # parte inicialmente sin fuerza aplicada

# =========================================================
# CONDICIONES INICIALES
# =========================================================
theta1_0_deg = 5.0
theta2_0_deg = 15.0

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
omega1 = sol[:, 2]
omega2 = sol[:, 3]

# =========================================================
# GRÁFICOS
# =========================================================
fig, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Ángulos
axes[0].plot(t, theta1, label=r'$\theta_1(t)$')
axes[0].plot(t, theta2, label=r'$\theta_2(t)$', linestyle='--')
axes[0].set_ylabel('Ángulo [rad]')
axes[0].set_title('Example 1.6 — Respuesta temporal')
axes[0].grid(True)
axes[0].legend()

# Velocidades angulares
axes[1].plot(t, omega1, label=r'$\dot{\theta}_1(t)$')
axes[1].plot(t, omega2, label=r'$\dot{\theta}_2(t)$', linestyle='--')
axes[1].set_xlabel('Tiempo [s]')
axes[1].set_ylabel('Velocidad angular [rad/s]')
axes[1].grid(True)
axes[1].legend()

plt.tight_layout()
plt.show()