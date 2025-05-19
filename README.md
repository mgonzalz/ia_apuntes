# **Modelo de Redes Neuronales para la Predicción de Supervivencia Clínica.**

Este proyecto aplica técnicas de inteligencia artificial para desarrollar un modelo capaz de **predecir la probabilidad de supervivencia de un paciente** en función de múltiples variables clínicas, bioquímicas, genéticas, sociodemográficas y económicas. El enfoque se basa en redes neuronales profundas y métodos avanzados de explicabilidad para garantizar que los resultados sean comprensibles y clínicamente relevantes.

## **Contexto.**

En el ámbito de la medicina personalizada, la capacidad de anticipar la evolución clínica de un paciente es fundamental para **mejorar la eficiencia del sistema sanitario** y optimizar la atención médica. Con el avance de los sistemas de información clínica, se generan volúmenes masivos de datos estructurados que pueden ser utilizados para **detectar patrones complejos** que escapan al análisis tradicional.

Este trabajo aborda ese reto, construyendo un modelo predictivo sobre una base de datos compuesta por 50.000 pacientes, con información distribuida en múltiples dimensiones: biomarcadores, antecedentes clínicos, estilo de vida, genética, economía y demografía.

## **Objetivo del proyecto.**

Desarrollar e interpretar un modelo de red neuronal que **prediga la variable binaria `vive`**, indicando si un paciente ha superado un periodo crítico tras diagnóstico o intervención, utilizando como entrada un conjunto integrado de variables clínicas y contextuales.

## **Enfoque aplicado.**

El desarrollo se ha estructurado en torno a las siguientes fases:

1. **Integración y preprocesamiento de datos heterogéneos** procedentes de seis tablas temáticas (clínica, genética, sociodemográfica, etc.).
2. **Diseño y entrenamiento de una red neuronal profunda**, utilizando técnicas de regularización (`dropout`, `batch normalization`) y ajuste de clases (`class_weight`) para manejar el fuerte desbalance del dataset.
3. **Evaluación comparativa** con modelos base como árboles de decisión y random forest.
4. **Análisis de interpretabilidad** mediante SHAP, desglosado por grupos de variables, para entender cómo cada dimensión afecta la predicción.
5. **Exploración de la aplicabilidad real**, con la propuesta de un visor de riesgo clínico (VIDE) como herramienta para su integración futura en entornos asistenciales.

## **Propuesta de valor.**

Este proyecto no solo predice con precisión la supervivencia, sino que lo hace de forma **explicable y responsable**, permitiendo que médicos y personal sanitario comprendan qué factores están influyendo en cada decisión del modelo. La explicabilidad se convierte así en un puente entre la inteligencia artificial y la práctica médica real.

## **Aplicación clínica potencial.**

Se propone la integración del modelo en entornos de:

- Triaje asistido
- Medicina preventiva poblacional
- Estratificación de riesgo para seguimiento crónico
- Visualización personalizada en consulta médica (mockup: VIDE)

Esta solución puede **complementar el juicio clínico**, alertar sobre casos de riesgo no evidentes, y apoyar la toma de decisiones médicas con respaldo algorítmico interpretado.

## **Licencia.**

Este proyecto se presenta con fines académicos. Su aplicación práctica requeriría validación clínica adicional y aprobación ética.
