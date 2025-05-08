# **CHANGELOG - Archivos CSV.**

Este changelog documenta los cambios aplicados sobre el dataset consolidado en sus distintas versiones, con el objetivo de mantener trazabilidad y transparencia en las transformaciones realizadas antes del modelado.

## **Versión 1.0.**

- Integración de todas las tablas (bioquímicos, clínicos, genéticos, sociodemográficos, económicos y estilo de vida) mediante el identificador `paciente_id`.
- Tratamiento de valores nulos: no se han detectado tras integración.
- Conversión y limpieza básica de variables numéricas con formato de texto. Adaptación de los decimales.
- No se ha eliminado ningún valor atípico (outlier). Se ha optado por mantener todos los registros originales por su posible relevancia clínica.
- Este dataset se utiliza como **versión base y referencia principal** para el modelado.

## **Versión 2.0.**

- Basado en la versión 1.0, se incorpora un paso adicional de **tratamiento de valores extremos** en variables numéricas seleccionadas.
- Se ha aplicado **winsorización** al 1er y 99º percentil en variables como `glucosa`, `colesterol`, `trigliceridos`, `creatinina`, `ingresos_mensuales` y `gastos_salud`.
- Objetivo: evaluar el impacto de los outliers en el rendimiento y estabilidad del modelo.
- Esta versión se utilizará para comparativas controladas entre datasets con y sin recorte de extremos.
