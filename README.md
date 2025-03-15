# Propensión de Compra de Vehículos.

## Introducción.

Este proyecto tiene como objetivo el desarrollo de un modelo de **propensión de compra de vehículos**, empleando técnicas avanzadas de aprendizaje automático para identificar clientes con alta probabilidad de adquirir un segundo automóvil. La investigación se ha basado en el análisis de datos históricos de clientes y sus patrones de compra, lo que permite segmentarlos en distintos grupos estratégicos para la optimización de las estrategias de negocio y marketing.

El presente trabajo ha sido desarrollado por **María González** como parte de una iniciativa de análisis predictivo aplicada a la industria automotriz. La investigación se fundamenta en los principios establecidos en el **Project Charter**, que define los siguientes objetivos clave:

- Desarrollar un modelo predictivo para estimar la probabilidad de recompra de un vehículo.
- Aplicar técnicas de segmentación de clientes para mejorar la personalización de estrategias comerciales.
- Implementar una solución visual interactiva mediante **Streamlit** para el análisis y la exploración de métricas.
- Construir un entorno de despliegue basado en **Docker** para facilitar la portabilidad y la escalabilidad del sistema.

## Estructura del Proyecto.

```plaintext
propensity-model
│── benchmarking     # Parámetros óptimos junto a resultados de los modelos.
│── data             # Conjunto de datos de entrenamiento y validación.
│── deployment       # Archivos para el despliegue.
│   │── docker       # Configuración y archivos de Docker.
│   │── app.py       # Aplicación Streamlit para visualización.
│── docs             # Información del proyecto.
│── help
│── models           # Modelos entrenados.
│── notebooks        # Aplicación metodología CRISP-DM.
│── results          # Informe final.
│── sqr
│── src              # Código fuente y scripts de procesamiento.
```

## Metodología de Investigación y Desarrollo.

El proceso de desarrollo del modelo ha seguido una metodología estructurada, que incluye:

1. **Recopilación y preprocesamiento de datos**: Análisis de fuentes de información relevantes, limpieza y transformación de datos.
2. **Exploración de datos (EDA)**: Identificación de patrones de comportamiento en la compra de vehículos.
3. **Ingeniería de características**: Creación de variables derivadas y selección de atributos relevantes para el modelo.
4. **Entrenamiento y evaluación de modelos**: Comparación de distintos algoritmos de clasificación, con optimización de hiperparámetros.
5. **Segmentación de clientes**: Clasificación en categorías estratégicas para la toma de decisiones comerciales.

## Implementación del Modelo Predictivo.

El modelo se ha entrenado utilizando **XGBoost** y **Random Forest**, entre otross, con un enfoque en la optimización de métricas clave como **AUC-ROC**, **precisión**, **recall** y **F1-score**. Los principales pasos implementados incluyen:

- Definición de un conjunto de entrenamiento y validación.
- Optimización de hiperparámetros mediante técnicas de búsqueda manual, no automáticas.
- Evaluación de métricas de desempeño en diferentes escenarios.
- Interpretación de la importancia de características mediante SHAP y Feature Importance.

## Integración y Visualización mediante Streamlit.

Se ha desarrollado una interfaz interactiva en **Streamlit** que permite:

- Cargar datos en tiempo real y visualizar predicciones de propensión de compra.
- Examinar métricas clave del modelo para la evaluación de su rendimiento.
- Analizar la segmentación de clientes y sus características demográficas y comportamentales.
- Generar reportes exportables para la toma de decisiones comerciales.

## Estrategias de Marketing Basadas en los Resultados.

A partir del modelo predictivo, se han diseñado estrategias de marketing para cada segmento:

- **Segmento Premium (85%+ de probabilidad):** Fidelización con eventos exclusivos, acceso prioritario a nuevos modelos y personalización de vehículos. Se prioriza la experiencia del cliente y recompra asegurada.
- **Segmento Potencial (55%-85% de probabilidad):** Retargeting con incentivos personalizados, financiamiento flexible y campañas automatizadas basadas en comportamiento de uso y kilometraje.
- **Segmento Intermedio (30%-55% de probabilidad):** Estrategias de conversión con descuentos estratégicos, pruebas de manejo con incentivos y beneficios en postventa (seguros, mantenimiento).
- **Segmento de Baja Propensión (<15% de probabilidad):** Contacto a bajo costo mediante campañas automatizadas, incentivos simbólicos como descuentos en accesorios y campañas educativas sobre financiamiento.

## Despliegue con Docker.

Se ha construido un entorno de despliegue utilizando **Docker**, lo que permite la ejecución de la solución en cualquier infraestructura sin configuraciones adicionales. Esto facilita la portabilidad y reproducibilidad del modelo y su integración en entornos productivos.

### Comandos para la ejecución en Docker.

```bash
cd deployment/docker
docker-compose up --build
```

Acceso a la aplicación en `http://localhost:8501`

Para detener el contenedor:

```bash
docker-compose down
```

## Conclusiones Finales.

El modelo de propensión de compra ha demostrado ser una herramienta efectiva para la optimización de estrategias comerciales en la industria automotriz. La integración de **Machine Learning**, **visualización interactiva** y **automatización con Docker** permite una solución escalable y adaptable a distintos entornos de negocio.

Las conclusiones clave incluyen:

- **Reducción de costos de adquisición de clientes** mediante segmentación avanzada.
- **Aumento en la tasa de conversión** a través de estrategias dirigidas.
- **Automatización y eficiencia** en la toma de decisiones comerciales mediante integración con herramientas de visualización.

Este enfoque basado en datos representa un avance significativo en la personalización de estrategias de marketing y en la eficiencia operativa del sector automotriz.
