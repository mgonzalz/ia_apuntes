# **Diccionario de Datos – Dataset Consolidado para Predicción de Supervivencia.**

Este documento presenta la estructura del dataset utilizado en el proyecto de predicción de supervivencia en pacientes, integrando múltiples fuentes de información clínica, sociodemográfica, económica, genética y bioquímica. Cada tabla representa una dimensión del paciente, y ha sido unificada a través del identificador único `paciente_id`.

A continuación, se describen las variables incluidas en el conjunto de datos, junto con su tipo de dato en origen y su naturaleza (categórica o continua), de acuerdo con su rol en el modelo de machine learning.

## **Tabla: Datos Bioquimico.**

Contiene indicadores bioquímicos obtenidos de análisis de sangre u otras muestras clínicas, relevantes para evaluar el estado fisiológico del paciente.

| Nombre de Columna     | Tipo de Dato | Naturaleza |
|------------------------|---------------|-------------|
| paciente_id            | nvarchar      | Identificador |
| glucosa                | float         | Continua      |
| colesterol             | float         | Continua      |
| trigliceridos          | float         | Continua      |
| hemoglobina            | float         | Continua      |
| leucocitos             | float         | Continua      |
| plaquetas              | float         | Continua      |
| creatinina             | float         | Continua      |

## **Tabla: Datos Clinicos.**

Incluye condiciones médicas preexistentes o diagnosticadas, útiles para caracterizar comorbilidades y antecedentes relevantes para el pronóstico.

| Nombre de Columna     | Tipo de Dato | Naturaleza |
|------------------------|---------------|-------------|
| paciente_id            | nvarchar      | Identificador |
| diabetes               | int           | Categórica   |
| hipertension           | int           | Categórica   |
| obesidad               | int           | Categórica   |
| cancer                 | int           | Categórica   |
| enfermedad_cardiaca    | int           | Categórica   |
| asma                   | int           | Categórica   |
| epoc                   | int           | Categórica   |

## **Tabla: Datos Geneticos.**

Contiene información binaria sobre la presencia de mutaciones genéticas relevantes asociadas a predisposición o progresión de enfermedades oncológicas y crónicas.

| Nombre de Columna     | Tipo de Dato | Naturaleza |
|------------------------|---------------|-------------|
| paciente_id            | nvarchar      | Identificador |
| mut_BRCA1              | int           | Categórica   |
| mut_TP53               | int           | Categórica   |
| mut_EGFR               | int           | Categórica   |
| mut_KRAS               | int           | Categórica   |
| mut_PIK3CA             | int           | Categórica   |
| mut_ALK                | int           | Categórica   |
| mut_BRAF               | int           | Categórica   |

## **Tabla: Datos Economicos.**

Agrupa variables relacionadas con la situación económica del paciente, potencialmente influyentes en el acceso a cuidados sanitarios y adherencia terapéutica.

| Nombre de Columna     | Tipo de Dato | Naturaleza |
|------------------------|---------------|-------------|
| paciente_id            | nvarchar      | Identificador |
| ingresos_mensuales     | nvarchar      | Continua (restringida como texto) |
| gastos_salud           | int           | Continua      |
| seguro_salud           | int           | Categórica   |
| deudas                 | int           | Categórica   |
| tipo_empleo            | nvarchar      | Categórica   |
| ayudas_publicas        | int           | Categórica   |

## **Tabla: Datos Generales.**

Registra aspectos del estilo de vida del paciente y contiene la variable objetivo del modelo (`vive`), que representa la supervivencia tras un periodo crítico.

| Nombre de Columna     | Tipo de Dato | Naturaleza |
|------------------------|---------------|-------------|
| paciente_id            | nvarchar      | Identificador |
| fumador                | int           | Categórica   |
| alcohol                | int           | Categórica   |
| actividad_fisica       | int           | Categórica   |
| vive                   | int           | **Objetivo (binaria)** |

## **Tabla: Datos Sociodemograficos.**

Describe características sociodemográficas fundamentales para segmentar y contextualizar al paciente dentro de su entorno social y geográfico.

| Nombre de Columna     | Tipo de Dato | Naturaleza |
|------------------------|---------------|-------------|
| paciente_id            | nvarchar      | Identificador |
| edad                   | int           | Continua      |
| sexo                   | nvarchar      | Categórica   |
| estado_civil           | nvarchar      | Categórica   |
| nivel_educativo        | nvarchar      | Categórica   |
| ocupacion              | nvarchar      | Categórica   |
| region                 | nvarchar      | Categórica   |
| pais_nacimiento        | nvarchar      | Categórica   |
| codigo_postal          | int           | Categórica (territorial) |
