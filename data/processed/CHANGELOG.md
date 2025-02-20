# CHANGELOG - Archivos CSV.

## **Versión 1.0.**

- Sustitución de valores nulos en las columnas **ESTADO_CIVIL, GENERO, ZONA_RENTA** por la **moda**.
- Transformación de variables categóricas:
  - **Ordinal Encoder** aplicado a **POTENCIA, ZONA_RENTA, AVERIA_GRAVE**.
  - **Label Encoder** aplicado al resto de variables categóricas.
- Tratamiento de valores atípicos en variables continuas:
  - Outliers definidos en los percentiles **0.10** y **0.90**.
  - Eliminación de filas con valores fuera de estos rangos.

## **Versión 2.0.**

- Sustitución de valores nulos en las columnas **ESTADO_CIVIL, GENERO** por la **moda**.
- En la columna **ZONA_RENTA**, los valores nulos han sido reemplazados por una nueva subcategoría llamada **"Desconocida"**.
Al aplicar **Ordinal Encoder**, esta nueva categoría se ha definido con el grado más bajo de prioridad.
- Transformación de variables categóricas:
  - **Ordinal Encoder** aplicado a **POTENCIA, ZONA_RENTA, AVERIA_GRAVE**.
  - **Label Encoder** aplicado al resto de variables categóricas.
- Tratamiento de valores atípicos en variables continuas:
  - Outliers definidos en los percentiles **0.10** y **0.90**.
  - Eliminación de filas con valores fuera de estos rangos.

## **Versión 3.0.**

- Eliminación total de filas con valores nulos en cualquier columna.
- Transformación de variables categóricas:
  - **Ordinal Encoder** aplicado a **POTENCIA, ZONA_RENTA, AVERIA_GRAVE**.
  - **Label Encoder** aplicado al resto de variables categóricas.
- Tratamiento de valores atípicos en variables continuas:
  - Outliers definidos en los percentiles **0.10** y **0.90**.
  - Eliminación de filas con valores fuera de estos rangos.

## **Versión 4.0.**

- Eliminación de filas con valores nulos en las columnas **ESTADO_CIVIL** y **GENERO**.
- En la columna **ZONA_RENTA**, los valores nulos han sido reemplazados por una nueva subcategoría llamada **"Desconocida"**.
Al aplicar **Ordinal Encoder**, esta nueva categoría se ha definido con el grado más bajo de prioridad.
- Transformación de variables categóricas:
  - **Ordinal Encoder** aplicado a **POTENCIA, ZONA_RENTA, AVERIA_GRAVE**.
  - **Label Encoder** aplicado al resto de variables categóricas.
- Tratamiento de valores atípicos en variables continuas:
  - Outliers definidos en los percentiles **0.10** y **0.90**.
  - Eliminación de filas con valores fuera de estos rangos.

## **Versión 5.0.**

- Eliminación de filas con valores nulos en las columnas **ESTADO_CIVIL** y **GENERO**.
- En la columna **ZONA_RENTA**, los valores nulos han sido reemplazados por la **moda**.
- Transformación de variables categóricas:
  - **Ordinal Encoder** aplicado a **POTENCIA, ZONA_RENTA, AVERIA_GRAVE**.
  - **Label Encoder** aplicado al resto de variables categóricas.
- Tratamiento de valores atípicos en variables continuas:
  - Outliers definidos en los percentiles **0.10** y **0.90**.
  - Eliminación de filas con valores fuera de estos rangos.
