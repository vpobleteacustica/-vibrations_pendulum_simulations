import numpy as np


def get_default_params():
    return {
        "m": 1.0,
        "L1": 1.0,
        "L2": 1.0,
        "g": 9.81,
        "F": 0.0
    }


def solve_accelerations_and_tension(theta1, theta2, omega1, omega2, params):
    m = params["m"]
    L1 = params["L1"]
    L2 = params["L2"]
    g = params["g"]
    F = params["F"]

    delta = theta2 - theta1
    s = np.sin(delta)
    c = np.cos(delta)

    # -----------------------------------------------------
    # Sistema A x = b
    # x = [theta1_ddot, theta2_ddot, T]
    # -----------------------------------------------------
    #
    # Ecuación 1:
    # F sin(theta2) + mg cos(theta2) - T cos(delta)
    # = m[L1 theta1_ddot sin(delta) - L1 omega1^2 cos(delta) - (L2/2) omega2^2]
    #
    # => m L1 s theta1_ddot + c T
    #    = F sin(theta2) + mg cos(theta2)
    #      + m L1 omega1^2 c + m (L2/2) omega2^2
    #
    # Ecuación 2:
    # F cos(theta2) - mg sin(theta2) + T sin(delta)
    # = m[L1 theta1_ddot cos(delta) + L1 omega1^2 sin(delta) + (L2/2) theta2_ddot]
    #
    # => m L1 c theta1_ddot + m (L2/2) theta2_ddot - s T
    #    = F cos(theta2) - mg sin(theta2) - m L1 omega1^2 s
    #
    # Ecuación 3:
    # F (L2/2) cos(theta2) - T (L2/2) sin(delta) = (mL2^2/12) theta2_ddot
    #
    # => (mL2^2/12) theta2_ddot + (L2/2) s T
    #    = F (L2/2) cos(theta2)

    A = np.array([
        [m * L1 * s,              0.0,               c],
        [m * L1 * c,      m * L2 / 2.0,             -s],
        [0.0,             m * L2**2 / 12.0,   (L2 / 2.0) * s]
    ], dtype=float)

    b = np.array([
        F * np.sin(theta2) + m * g * np.cos(theta2)
        + m * L1 * omega1**2 * c
        + m * (L2 / 2.0) * omega2**2,

        F * np.cos(theta2) - m * g * np.sin(theta2)
        - m * L1 * omega1**2 * s,

        F * (L2 / 2.0) * np.cos(theta2)
    ], dtype=float)

    # chequeo de condicionamiento
    if np.linalg.cond(A) > 1e12:
        raise ValueError(
            "La matriz del sistema está mal condicionada o casi singular. "
            "Prueba otras condiciones iniciales."
        )

    x = np.linalg.solve(A, b)

    theta1_ddot = x[0]
    theta2_ddot = x[1]
    T = x[2]

    return theta1_ddot, theta2_ddot, T


def dynamics(t, y, params):
    theta1, theta2, omega1, omega2 = y

    theta1_ddot, theta2_ddot, _ = solve_accelerations_and_tension(
        theta1, theta2, omega1, omega2, params
    )

    return np.array([omega1, omega2, theta1_ddot, theta2_ddot], dtype=float)