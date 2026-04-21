import numpy as np

def euler_step(f, t, y, dt):
    """
    Método de Euler explícito
    """
    return y + dt * f(t, y)


def rk4_step(f, t, y, dt):
    """
    Método de Runge-Kutta de orden 4
    """
    k1 = f(t, y)
    k2 = f(t + dt/2, y + dt*k1/2)
    k3 = f(t + dt/2, y + dt*k2/2)
    k4 = f(t + dt, y + dt*k3)

    return y + (dt/6)*(k1 + 2*k2 + 2*k3 + k4)


def simulate(f, y0, t):
    """
    Integrador general usando RK4

    Parameters
    ----------
    f : function
        Función dinámica
    y0 : array
        Condición inicial
    t : array
        Vector de tiempo

    Returns
    -------
    y : array
        Solución en el tiempo
    """
    y = np.zeros((len(t), len(y0)))
    y[0] = y0

    for i in range(len(t) - 1):
        dt = t[i+1] - t[i]
        y[i+1] = rk4_step(f, t[i], y[i], dt)

    return y