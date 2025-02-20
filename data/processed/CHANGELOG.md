# CHANGELOG - Archivos CSV.

## **Versión 1.0.**

- Sustitución de valores nulos en las columnas **ESTADO_CIVIL, GENERO, ZONA_RENTA** por la **moda**.
- Transformación de variables categóricas:
  - **Ordinal Encoder** aplicado a **POTENCIA, ZONA_RENTA, AVERIA_GRAVE**.
  - **Label Encoder** aplicado al resto de variables categóricas.
- Tratamiento de valores atípicos en variables continuas:
  - Outliers definidos en los percentiles **0.10** y **0.90**.
  - Eliminación de filas con valores fuera de estos rangos.
