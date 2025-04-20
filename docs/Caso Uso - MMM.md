# **Caso de Uso: Predicción de Tráfico Web y Optimización de Inversión Publicitaria en Retail.**

## **Relación entre Objetivo 1 y Objetivo 2.**

Este caso de uso aborda dos objetivos interrelacionados, aplicando técnicas de series temporales y modelización de atribución publicitaria para optimizar la inversión en marketing y maximizar el impacto en ventas y tráfico.

### **Objetivo 1: Predicción del Tráfico Web.**

**Propósito**: Estimar el número de visitantes únicos a la web (`Unique_visitors`) durante los próximos 6 meses mediante un modelo de series temporales SARIMA.

**Datos involucrados**:

- Tabla `WEB`: `Unique_visitors`.
- Tabla `TIME`: variables exógenas como `working_days`, `Dias_fines_semana`, `Easterweek`.

**Modelo sugerido**: SARIMA, incorporando:

- Tendencia, estacionalidad y ruido,
- Regresores exógenos (eventos y calendario).

**Métricas de evaluación**:

- MSE (Error Cuadrático Medio),
- AIC (Criterio de Información de Akaike).

> Recomendación: No es necesario un EDA exhaustivo, se prioriza la descomposición de la serie, la identificación de parámetros y la calidad del pronóstico.

**Resultado clave**: una serie forecast de `Unique_visitors` a futuro.

### **Objetivo 2: Modelo de Atribución Publicitaria (MMM).**

**Propósito**: Estimar el impacto de la inversión publicitaria en los resultados comerciales y optimizar la distribución del presupuesto entre canales.

### **Elección de la Variable Objetivo (`y`)**

| Variable              | Qué mide                                             | Cuándo usarla                                  |
|-----------------------|------------------------------------------------------|-------------------------------------------------|
| `Visit_Store`         | Tráfico físico a tienda (personas que entran)       | Si se quiere **atraer visitas a tienda**        |
| `Sales`               | Ventas totales (número de transacciones en tienda)  | Si se busca **maximizar ventas**               |
| `Sales / Visit_Store`| Tasa de conversión (eficacia de las visitas)        | Si se desea analizar la **eficiencia** del canal|

**Recomendación**:

- Usar `Sales` como variable objetivo principal, ya que representa directamente el éxito comercial.
- Se puede complementar con el análisis de `Sales / Visit_Store` si se desea profundizar en la conversión.

### **Variables explicativas**:

- Publicidad (`INV`): INTERNET, RADIO, PLATAFORMAS VIDEO, etc.
- Factores temporales (`TIME`).
- `Unique_visitors` (resultado del Objetivo 1 o histórico durante el entrenamiento).

### **¿Por qué incluir `Unique_visitors` como variable explicativa?**

Aunque `Unique_visitors` es la variable objetivo del Objetivo 1, también debe utilizarse como variable explicativa en el modelo del Objetivo 2, por las siguientes razones:

- La publicidad muchas veces no impacta directamente en las ventas, sino a través de un paso intermedio: el tráfico web.
- Es decir, muchos clientes **primero visitan la web** antes de comprar en tienda.

> Publicidad → Visitas Web → Visitas Tienda → Ventas

Al incluir `Unique_visitors` en el modelo:

```python
Sales = B0 + B1*INTERNET + B2*RADIO + B3*Unique_visitors + error
```

- Se mejora la capacidad explicativa del modelo.
- Se refleja mejor el recorrido real del cliente (customer journey).

Si no se incluye:

- El modelo asumiría que la inversión impacta directamente en ventas,
- Ignorando una parte importante del efecto mediado por lo digital.

### **Modelo sugerido**:

- Regresión múltiple o Ridge Regression (por multicolinealidad),
- Con delays mínimos (por tamaño reducido del dataset: 36 observaciones).

### **Condiciones**:

- Coeficientes deben tener lógica de negocio (positivos para inversión),
- Incorporar saturación o rendimiento decreciente si aplica.

### **Simulación y optimización**:

- Redistribuir el presupuesto de 2024 (primeros 6 meses con +15%),
- Encontrar el punto óptimo de inversión por canal,
- Evaluar escenarios para maximizar `y` (ventas, tráfico o conversión).

### **Cuándo usar valores reales vs. forecast de `Unique_visitors`**

| Escenario                         | `Unique_visitors` a usar         | Justificación                          |
|----------------------------------|----------------------------------|----------------------------------------|
| Entrenamiento del modelo         | Reales (de la tabla WEB)         | Estás usando datos pasados             |
| Simulación futura (presupuesto)  | Forecast (modelo SARIMA)         | Aún no existen los datos reales futuros|

Esto permite entrenar con datos observados, y luego simular escenarios futuros con los valores previstos por el modelo SARIMA del Objetivo 1.

### **Conexión entre Objetivos.**

1. **El tráfico web forecast (Objetivo 1)** se utiliza como input en el modelo de atribución (Objetivo 2).
2. **La inversión publicitaria afecta al tráfico web**, y este, a su vez, **impacta en visitas a tienda y ventas**.
3. El modelo completo refleja una cadena de causalidad de marketing:
   > Publicidad → Tráfico Web → Tráfico Tienda/Ventas

## **Enfoque Metodológico General.**

1. **Modelado de serie temporal SARIMA** sobre `Unique_visitors`.
2. **Construcción de modelo de atribución** con regresores publicitarios y tráfico forecast.
3. **Optimización del presupuesto** con simulaciones bajo distintos escenarios.
