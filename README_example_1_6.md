# ACUS125 Aislamiento y Análisis de Vibraciones — Barra Rígida Suspendida (Ejemplo 1.6)

## Objetivo

En esta actividad extendemos el análisis a un sistema con **dos grados de libertad**, correspondiente al **Ejemplo 1.6 (Meirovitch)**.

A diferencia del Example 1.5, ahora el sistema requiere describirse mediante **dos coordenadas angulares**.

---

## Descripción del sistema

Se tiene:

- Una cuerda de longitud $L_1$
- Una barra rígida de longitud $L_2$ y masa $m$
- Un punto de suspensión $O$
- Una fuerza horizontal $F$ aplicada en el extremo de la barra

---

## Coordenadas generalizadas

Se definen dos ángulos:

- $\theta_1$: ángulo de la cuerda
- $\theta_2$: ángulo de la barra

El sistema tiene entonces:

$q = [\theta_1, \theta_2]$

---

## Idea clave

A diferencia del Example 1.5:

| Example 1.5 | Example 1.6 |
|------------|------------|
| 1 grado de libertad | 2 grados de libertad |
| 1 ecuación | Sistema de ecuaciones |
| Dinámica simple | Dinámica acoplada |

---

## Ecuaciones de movimiento (idea general)

El movimiento del sistema se describe mediante:

$M(q) \ddot{q} + C(q, \dot{q}) + G(q) = Q$

donde:

- $M(q)$: matriz de masa
- $C(q, \dot{q})$: términos no lineales
- $G(q)$: efectos de gravedad
- $Q$: fuerzas externas

---

## Presencia de la tensión $T$

En el desarrollo aparece una fuerza interna:

- tensión en la cuerda $T$

Esta **no es de interés directo**, por lo que se elimina del sistema.

---

## Interpretación física

- $\theta_1$ controla el movimiento del punto de unión
- $\theta_2$ describe la orientación de la barra
- Ambos movimientos están **acoplados**

---

## Qué se explorará

En este ejemplo:

- Evolución de $\theta_1(t)$ y $\theta_2(t)$
- Interacción entre ambos ángulos
- Respuesta del sistema ante fuerza $F$
- Diferencia entre sistemas simples y acoplados

---

## Cómo ejecutar

```bash
python scripts/simulation_example_1_6_time_response.py
```

```bash
python scripts/simulation_example_1_6_animation.py
```

---

## Idea clave final

> A medida que aumentan los grados de libertad, los sistemas físicos requieren modelos más complejos y soluciones numéricas.

---

## Conexión con Example 1.5

- Example 1.5 → base conceptual
- Example 1.6 → extensión a sistemas acoplados

Ambos forman parte del mismo marco de dinámica de sistemas vibratorios.

