# ACUS125 Aislamiento y Análisis de Vibraciones — Péndulo Compuesto (Ejemplo 1.5)

## Objetivo

En esta actividad retomamos el **Ejemplo 1.5 (Meirovitch)** y lo extendemos desde un **análisis en un instante** a un **modelo dinámico completo** que podemos simular.

---

## Problema (visto en clases)

Una barra rígida uniforme de longitud $L$ y masa $m$ está articulada en un punto $O$, ubicado a una distancia $L/6$ del centro de masa $C$.

El sistema se libera desde el reposo en la **posición horizontal**.

Se pide determinar la **aceleración angular inmediatamente después de la liberación**.

---

## Paso 1 — Ecuación de momentos (como en clases)

$\sum M_O = I_O \alpha$

El momento de fuerza debido al peso es:

$M_O = -mg \frac{L}{6}$

El momento de inercia respecto a $O$ es:

$I_O = \frac{mL^2}{9}$

---

## Paso 2 — Resultado obtenido en clases

$\alpha = -\frac{3g}{2L}$

---

## Aclaración importante

Este resultado es válido **sólo en el instante de liberación**, cuando la barra está **horizontal**.

En ese instante:

$\theta = 90^\circ \quad \Rightarrow \quad \sin(\theta) = 1$

---

## Paso 3 — Modelo dinámico general

Cuando la barra comienza a moverse, el torque depende del ángulo $\theta$.

La expresión correcta del momento de fuerza es:

$M_O = -mg \left(\frac{L}{6}\right)\sin(\theta)$

Entonces, la ecuación de movimiento es:

$I_O \ddot{\theta} = -mg \frac{L}{6}\sin(\theta)$

Reemplazando $I_O$:

$\ddot{\theta} = -\frac{3g}{2L}\sin(\theta)$

---

## Idea clave

- El libro entrega una **aceleración angular en un instante específico**
- El modelo dinámico describe **la evolución completa del sistema**

---

## Aproximación lineal (ángulos pequeños)

Para ángulos pequeños:

$\sin(\theta) \approx \theta$

Entonces:

$\ddot{\theta} = -\frac{3g}{2L}\theta$

Este es un **sistema lineal** (movimiento armónico simple)

---

## Interpretación final

| Modelo | Ecuación | Significado |
|------|--------|--------|
| Resultado del libro | $\alpha = -\frac{3g}{2L}$ | Instante inicial |
| Modelo no lineal | $ \ddot{\theta} = -\frac{3g}{2L}\sin(\theta) $ | Física real |
| Modelo lineal | $\ddot{\theta} = -\frac{3g}{2L}\theta $ | Aproximación |

---

## Qué se explorará

En este proyecto:

- Simular el movimiento del péndulo compuesto
- Comparar modelos lineales y no lineales
- Identificar cuándo falla la aproximación lineal
- Visualizar la evolución angular

---

## Cómo ejecutar

```bash
python simulation_compound_pendulum.py
```

```bash
python simulation_linear_vs_nonlinear.py
```

---

## Idea final

> La diferencia entre un **valor puntual** y una **ecuación dinámica** es lo que permite simular sistemas vibratorios.
