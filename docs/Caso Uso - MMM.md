# **Caso de Uso: Predicción de Tráfico Web, Visitas a Tienda y Ventas Físicas en Retail.**

## **Relación entre Objetivo 1 y Objetivo 2.**

Este caso de uso aborda dos objetivos interrelacionados, aplicando técnicas de series temporales y modelización de atribución publicitaria para optimizar la inversión en marketing y maximizar el impacto tanto en el tráfico como en los resultados comerciales.

La conexión entre ambos objetivos es fundamental para construir un modelo lógico de atribución completo:

1. El **tráfico web forecast (Objetivo 1)** se utiliza como input en el modelo de visitas a tienda (Objetivo 2.1).
2. Las **visitas estimadas a tienda** se utilizan como input para estimar las ventas (Objetivo 2.2).
3. Se construye así una cadena causal completa:
   > Publicidad → Tráfico Web → Visitas a Tienda → Ventas

## **Objetivo 1: Predicción del Tráfico Web.**

**Propósito**: Estimar el número de visitantes únicos a la web (`Unique_visitors`) durante los próximos 6 meses mediante un modelo de series temporales SARIMA.

**Datos involucrados**:

- Tabla `WEB`: `Unique_visitors`.
- Tabla `TIME`: variables exógenas como `working_days`, `Dias_fines_semana`, `Easterweek`.

**Modelo sugerido**: SARIMA, incorporando:

- Tendencia, estacionalidad y ruido.
- Regresores exógenos (eventos y calendario).

**Métricas de evaluación**:

- MSE (Error Cuadrático Medio),
- AIC (Criterio de Información de Akaike).

> Recomendación: No es necesario un EDA exhaustivo. Se prioriza la descomposición de la serie, la identificación de parámetros y la calidad del pronóstico.

**Resultado clave**: una serie forecast de `Unique_visitors` a futuro.

## **Objetivo 2: Modelo en dos etapas - Visitas a tienda y ventas.**

### **Etapa 1: Modelo de Visitas a Tienda (`Visit_Store`).**

**Propósito**: Estimar el impacto de la inversión publicitaria y el tráfico web en el tráfico físico a tienda (`Visit_Store`).

**Variable objetivo (`y`)**: `Visit_Store`.

**Variables explicativas**:

- `Budget_Online`.
- `Budget_Offline`.
- `Budget_Otros`.
- `Unique_visitors`.
- Variables Exógenas.

**Modelo sugerido**: Regresión múltiple o Ridge Regression (si hay multicolinealidad).

**Fórmula base del modelo 1**:

```python
Visit_Store_t = β0 \
              + β1 * Budget_Online \
              + β2 * Budget_Offline \
              + β3 * Budget_Otros \
              + β4 * Unique_visitors \
              + β5 * DirectTraffic \
              + β6 * v_exógena1_t \
              + β7 * v_exógena2_t \
              + ... +
              + error
```

> Este modelo permite conocer qué canales y variables explicativas generan mayor volumen de visitas físicas en tienda, permitiendo una optimización posterior de medios.

### **Etapa 2: Modelo de Ventas (`Sales`) a partir de `Visit_Store`.**

**Propósito**: Estimar las ventas mensuales a partir del tráfico físico a tienda.

**Variable objetivo (`y`)**: `Sales`.

**Variables explicativas**:

- `Visit_Store_t`.
- Variables Exógenas.

**Modelo sugerido**: Regresión lineal simple o múltiple, según resultados.

**Fórmula base del modelo 2**:

```python
Sales_t = α0 \
        + α1 * Visit_Store_t \
        + α2 * v_exógena1_t \
        + α3 * v_exógena2_t \
        + α4 * v_exógena3_t \
        + ... +
        + error
```

> Esta segunda etapa añade una capa de realismo al customer journey: de la inversión a la visita, y de la visita a la compra.

### **Razón del enfoque en dos etapas.**

- Refleja mejor la cadena causal del comportamiento del consumidor:
  > Publicidad → Tráfico Web → Visitas a Tienda → Ventas

- Permite identificar cuánto influye la publicidad en cada fase del proceso.
- Aporta flexibilidad al análisis (se puede optimizar por fases).
- A largo plazo, este enfoque permitirá hacer seguimiento del embudo completo de conversión.

### **Simulación y optimización.**

- Se parte del presupuesto de 2024.
- Aplicar aumentos del 15%, 21% y 25% según el escenario.
- Repartir el presupuesto por canal (%).
- Utilizar `Unique_visitors` forecast para alimentar la primera etapa.
- Usar las predicciones de `Visit_Store` para estimar `Sales`.

### **Cuándo usar valores reales vs. forecast.**

| Escenario                         | Datos de `Unique_visitors`     | Datos de `Visit_Store`          |
|----------------------------------|--------------------------------|---------------------------------|
| Entrenamiento del modelo         | Reales                         | Reales                          |
| Simulación futura (presupuesto)  | Forecast (SARIMA)              | Estimado (modelo 1)             |

## **Enfoque Metodológico General.**

1. Modelado SARIMA para `Unique_visitors`.
2. Modelo de regresión para `Visit_Store` con marketing y web.
3. Modelo de `Sales` en función de `Visit_Store`.
4. Simulación y optimización de escenarios futuros.
