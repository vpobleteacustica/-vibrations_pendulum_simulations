# Análisis e Interpretación — Example 1.5 y Example 1.6

---

# Example 1.5 — Péndulo compuesto

## Modelo dinámico

Para ángulo general:

$\ddot{\theta} = -\frac{3g}{2L} \sin(\theta)$

Para pequeños ángulos:

$\ddot{\theta} \approx -\frac{3g}{2L} \theta$

---

## Interpretación

- Sistema de **1 grado de libertad**
- Sólo una variable: $\theta(t)$
- Movimiento completamente descrito por una sola ecuación

---

## Comparación: lineal vs no lineal

### Modelo no lineal
- Usa $ \sin(\theta) $
- Más realista
- Periodo depende de amplitud

### Modelo lineal
- Usa $ \theta $
- Aproximación válida solo para ángulos pequeños
- Periodo constante

---

## Qué observar en la simulación

- Para ángulos pequeños:
  - ambos modelos coinciden

- Para ángulos grandes:
  - aparece desfase
  - cambia el periodo

---

## Idea clave

> Un modelo lineal es una aproximación válida solo dentro de cierto rango.

---

# Example 1.6 — Barra rígida suspendida

## Modelo dinámico

Sistema con dos coordenadas:

$q = [\theta_1, \theta_2]$

- $\theta_1 $: ángulo de la cuerda
- $\theta_2 $: ángulo de la barra

---

## Diferencia fundamental con Example 1.5

| Example 1.5 | Example 1.6 |
|------------|------------|
| 1 DOF | 2 DOF |
| 1 ecuación | sistema acoplado |
| simple | complejo |

---

## 🔵 Interpretación de los gráficos

### Panel superior: ángulos

- $\theta_1(t)$: movimiento de la cuerda
- $\theta_2(t)$: rotación de la barra

Observaciones:

- no son iguales
- existe desfase
- presentan distinta frecuencia

Esto indica:

> El sistema es acoplado pero no simétrico.

---

### Panel inferior: velocidades angulares

- $ \dot{\theta}_2 $ suele tener mayor amplitud
- la barra rota más rápidamente

---

## Fenómeno observado

**Acoplamiento dinámico**

- la cuerda influye en la barra
- la barra influye en la cuerda
- el movimiento no es independiente

---

## Interpretación física clave

- la cuerda controla la posición del sistema
- la barra introduce dinámica rotacional adicional
- el sistema combina:
  - traslación
  - rotación

---

## Interpretación de la animación

Elementos:

- punto negro → pivote
- línea azul → cuerda
- línea naranja → barra
- punto rojo → centro de masa

Observaciones:

- la cuerda oscila suavemente
- la barra tiene movimiento más complejo
- el centro de masa describe trayectorias no triviales

---

## Conexión gráfico ↔ animación

- lo que se ve en \( \theta(t) \)
- se refleja directamente en la geometría

Esto valida el modelo

---

## Consideraciones numéricas

Este sistema es:

- no lineal
- acoplado
- sensible a condiciones iniciales

### Problemas posibles:

- overflow
- NaN
- inestabilidad numérica

### Soluciones:

- usar paso pequeño:

$dt = 0.001$

- usar ángulos iniciales pequeños:

$\theta_1 \approx 5^\circ, \quad \theta_2 \approx 15^\circ$

---

## Idea clave final

> A medida que aumentan los grados de libertad, los sistemas físicos presentan comportamientos emergentes que no pueden entenderse con una sola ecuación.

---

# Comparación global

| Característica | Example 1.5 | Example 1.6 |
|--------------|------------|------------|
| DOF | 1 | 2 |
| Tipo | simple | acoplado |
| Linealización | posible | limitada |
| Complejidad | baja | alta |
| Simulación | directa | requiere sistema |

---

# Conclusión general

- Example 1.5 introduce dinámica básica
- Example 1.6 introduce sistemas acoplados
- ambos son fundamentales para entender vibraciones reales

---

# Mensaje final

> La complejidad del sistema vibratorio no depende sólo de las fuerzas, sino del número de variables que describen su movimiento (grados de libertad).