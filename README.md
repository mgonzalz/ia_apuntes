# **Marketing Mix Modeling (MMM) para Retail: Predicción y Simulación de Escenarios Publicitarios.**

Este proyecto implementa un sistema completo de atribución publicitaria y simulación de escenarios de inversión para el canal retail. Basado en datos históricos de tráfico, inversión y ventas, el objetivo es optimizar el presupuesto publicitario mediante un pipeline automatizado de predicción y análisis.

## **Objetivo General.**

Desarrollar un modelo de atribución que relacione la inversión publicitaria con el tráfico web, las visitas físicas y las ventas, permitiendo:

- Estimar el impacto real de cada canal de inversión (online, offline, otros).
- Predecir el comportamiento comercial futuro (tráfico y ventas).
- Simular múltiples estrategias de asignación presupuestaria.
- Identificar combinaciones óptimas de inversión bajo criterios de eficiencia.

## **Fases del Proyecto.**

**1. Análisis Exploratorio y Preparación de Datos.**
    - Limpieza, transformación y estructura final del dataset.
    - Análisis de estacionalidad, campañas y comportamiento temporal.

**2. Modelado Predictivo.**

- SARIMA para predicción de tráfico digital (`Unique_visitors`) a 24 meses.
- Regresión múltiple para estimación de visitas físicas (`Visit_Store`).
- Modelo de ventas basado en visitas físicas y eventos comerciales.

**3. Simulación de Escenarios.**

- Cuatro escenarios proyectados: A (Digital), B (Balanceado), C (Tradicional), y Base (distribución plana).
- Simulación presupuestaria sobre base 2024 con incrementos +15%, +21%, +25%.
- Aplicación del pipeline de modelos a escenarios simulados para predicción futura (2025–2026).

**4. Evaluación y Selección del Escenario Óptimo.**

- Métrica principal: Ratio de conversión `Sales / Visit_Store`.
- Análisis de eficiencia, saturación y retorno por canal.
- Comparación entre escenarios simulados y el modelo base.

## **Tecnologías y Herramientas.**

- **Python**, **Pandas**, **Statsmodels**, **Scikit-learn**, **Matplotlib**, **Seaborn**
- Forecasting con **SARIMA**
- Visualización de resultados y simulaciones
- Automatización y modularización del código
- Integración futura con **Docker** y **n8n** para despliegue

## **Resultados Clave.**

- El modelo logra predecir tráfico y ventas con una lógica de negocio sólida, validada por la evolución de la métrica de conversión.
- El **Escenario B (Balanceado)** presenta el mejor compromiso entre inversión, retorno y eficiencia general.
- La comparación entre escenarios muestra un incremento de hasta **+59% en ventas totales** frente al modelo base.
- Se ha calculado el punto de saturación para evitar inversión ineficiente, y se ha diseñado un **roadmap estratégico** con 5 fases de implantación.

## **Recomendaciones Estratégicas.**

- Redistribuir la inversión con mayor peso en digital sin descuidar la presencia offline.
- Reforzar campañas en momentos clave como **Rebajas**, **Navidad** o **Fin de Mes**, aprovechando el comportamiento histórico y los coeficientes del modelo.
- Utilizar las métricas generadas para alimentar un sistema de decisiones dinámico y escalable.

## **Consideraciones Finales.**

Este sistema ofrece una solución modular, explicativa y basada en datos para decisiones comerciales estratégicas. Está diseñado para integrarse en entornos reales mediante herramientas de automatización (Docker, pipelines, agentes N8N) y visualización en dashboards de negocio.

> El enfoque no se limita a predecir, sino a simular, optimizar y tomar decisiones sostenibles sobre el mix de medios.
