# Vibraciones — Simulación Numérica e Interpretación Física

## Contexto del curso

Este repositorio forma parte del curso:

**ACUS125 — Aislamiento y Análisis de Vibraciones**

Su propósito es apoyar el aprendizaje mediante:

- simulación numérica  
- visualización  
- interpretación física  

---

## Objetivo

Comprender el comportamiento de sistemas vibratorios combinando:

- modelamiento analítico  
- integración numérica  
- análisis gráfico  

---

## Contenidos

Este repositorio incluye dos ejemplos fundamentales basados en Meirovitch:

---

### Example 1.5 — Péndulo compuesto

- Sistema de **1 grado de libertad (1 DOF)**  
- Modelo no lineal:

$\ddot{\theta} = -\frac{3g}{2L}\sin(\theta)$

- Aproximación lineal:

$\ddot{\theta} = -\frac{3g}{2L}\theta$

Conceptos clave:

- diferencia entre modelo lineal y no lineal  
- validez de aproximaciones  
- dependencia del período con la amplitud  

---

### Example 1.6 — Sistema acoplado

- Sistema de **2 grados de libertad (2 DOF)**  

Coordenadas:

- $\theta_1 $: ángulo de la cuerda  
- $\theta_2 $: ángulo de la barra  

Conceptos clave:

- acoplamiento dinámico  
- interacción entre variables  
- comportamiento emergente  

---

## Estructura del proyecto

```text
.
├── scripts/
│   ├── simulation_compound_pendulum.py
│   ├── simulation_linear_vs_nonlinear.py
│   ├── simulation_example_1_6_time_response.py
│   └── simulation_example_1_6_animation.py
├── utils/
│   ├── integrators.py
│   └── example_1_6_dynamics.py
├── exercises/
│   ├── questions.md
│   └── questions_example_1_6.md
├── analysis_notes.md
├── README.md
└── requirements.txt
```

---

## Cómo ejecutar

Desde la carpeta raíz del proyecto:

```bash
python scripts/simulation_compound_pendulum.py
```

```bash
python scripts/simulation_linear_vs_nonlinear.py
```

```bash
python scripts/simulation_example_1_6_time_response.py
```

```bash
python scripts/simulation_example_1_6_animation.py
```

---

## Enfoque de aprendizaje

Este repositorio está diseñado para la **exploración activa**.

Se recomienda:

- modificar condiciones iniciales  
- cambiar parámetros del sistema  
- comparar modelos  
- relacionar ecuaciones con el movimiento observado  

---

## Idea clave

> Comprender vibraciones no es solo resolver ecuaciones,  
> sino interpretar cómo evolucionan los sistemas en el tiempo.

---

## Nota del profesor

Se espera que los estudiantes:

- conecten teoría y simulación  
- identifiquen cuándo un modelo es válido  
- interpreten correctamente los gráficos  

---

## Experimentos sugeridos

Prueba modificar:

```python
theta0_deg = 5
theta0_deg = 80
```

En Example 1.6:

```python
theta1_0_deg = 5
theta2_0_deg = 30
```

Observa:

- diferencias entre modelos  
- efectos de acoplamiento  
- limitaciones de las aproximaciones  

---

## Material complementario

Revisar:

- `analysis_notes.md` → interpretación física  
- `exercises/` → actividades guiadas  

---

## Mensaje final

> El análisis de vibraciones se comprende mejor cuando ecuaciones, simulaciones e intuición trabajan juntas.
