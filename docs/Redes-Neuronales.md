# **Fundamentos Teóricos y Recomendaciones Técnicas: Redes Neuronales para Predicción Clínica.**

Este documento sintetiza los fundamentos teóricos de las redes neuronales aplicadas a problemas de clasificación binaria, como la predicción de supervivencia en pacientes, y establece las recomendaciones técnicas apropiadas para su implementación en entornos sanitarios con datos estructurados.

## **Preprocesamiento de Datos para Redes Neuronales.**

Antes de aplicar cualquier modelo de red neuronal, los datos deben cumplir ciertos requisitos técnicos fundamentales:

- **Unificación estructural**: las distintas fuentes deben integrarse mediante un identificador único (`paciente_id`), generando una matriz rectangular (filas = pacientes, columnas = variables).
- **Codificación de variables categóricas**: variables como sexo, estado civil o tipo de empleo deben convertirse a formato numérico mediante técnicas como *One-Hot Encoding* o *Label Encoding*.
- **Normalización o estandarización**: las variables numéricas deben escalarse (por ejemplo, con `StandardScaler` o `MinMaxScaler`) para mejorar la estabilidad del aprendizaje.
- **Gestión de valores ausentes**: los valores nulos deben tratarse mediante imputación (media, moda, regresión) o eliminación controlada.
- **Balanceo de clases**: en caso de que la variable objetivo esté desbalanceada (ej. vive=1 en solo el 20% de los casos), se deben aplicar técnicas de sobremuestreo o submuestreo.
- **Separación en conjuntos de entrenamiento y validación**: es crucial dividir los datos antes del entrenamiento (por ejemplo, 80% entrenamiento, 20% validación), idealmente con *estratificación*.

## **Arquitectura de las Redes Neuronales.**

Una red neuronal multicapa (MLP) es la estructura más común para problemas con datos tabulares como los clínicos. **Componentes:**

- **Capa de entrada**: una neurona por variable predictora.
- **Capas ocultas**: permiten aprender relaciones no lineales. Usualmente entre 1 y 3 capas ocultas.
- **Capa de salida**: una única neurona con activación sigmoidea para problemas binarios.

## **Funciones de Activación**

Introducen no linealidad en el modelo. Las más utilizadas son:

| Función     | Fórmula                            | Aplicación típica              |
|-------------|-------------------------------------|--------------------------------|
| **ReLU**    | $f(x) = \max(0, x)$             | Capas ocultas (estándar)       |
| Sigmoidea   | $f(x) = \frac{1}{1 + e^{-x}}$   | Capa de salida binaria         |
| Tanh        | $f(x) = \tanh(x)$               | Alternativa a ReLU             |
| Softmax     | Función exponencial normalizada     | Clasificación multiclase       |

## **Funciones de Pérdida.**

Determinan el error durante el entrenamiento. Según el tipo de problema, se elige:

| Función                | Aplicación                           |
|------------------------|--------------------------------------|
| **Binary Cross-Entropy** | Clasificación binaria (vive/no vive) |
| MSE (Error cuadrático medio) | Problemas de regresión             |
| Categorical Cross-Entropy | Clasificación multiclase           |

## **Optimizadores.**

Controlan cómo se actualizan los pesos de la red neuronal.

| Optimizador | Características                                       | Uso frecuente |
|-------------|--------------------------------------------------------|----------------|
| **Adam**    | Estabilidad y convergencia rápida                     | Estándar en modelos modernos |
| SGD         | Simplicidad, sensible al aprendizaje                   | Poco frecuente sin ajustes     |
| RMSprop     | Recomendado en secuencias o RNNs                      | Casos específicos              |

## **Regularización y Control de Sobreajuste.**

| Técnica         | Descripción                                                         | Recomendación |
|------------------|----------------------------------------------------------------------|----------------|
| **Dropout**       | Apaga aleatoriamente un % de neuronas en cada batch                | Alta eficacia |
| L2 (Ridge)        | Penaliza pesos grandes, reduce complejidad                         | Estándar     |
| Early Stopping    | Detiene entrenamiento cuando la validación deja de mejorar         | Recomendado  |

## **Evaluación del Modelo.**

**Métricas clave.**

- **Accuracy**: proporción total de aciertos.
- **Precision, Recall, F1-score**: especialmente útiles en clases desbalanceadas.
- **AUC-ROC**: capacidad de distinguir correctamente entre clases.

**Validación cruzada:** Técnica esencial para medir la capacidad de generalización del modelo.

## **Técnicas de Balanceo de Clases.**

Cuando una clase (por ejemplo, los pacientes que sobreviven) es mucho menor que la otra, se aplican:

| Técnica            | Descripción                                                  |
|--------------------|--------------------------------------------------------------|
| **SMOTE**          | Genera instancias sintéticas interpolando puntos reales       |
| Random Oversampling| Duplica instancias reales de la clase minoritaria            |
| Random Undersampling| Elimina ejemplos de la clase mayoritaria                    |
| SMOTE + ENN / Tomek| Combinaciones que suavizan las fronteras de clasificación     |

## **Hiperparámetros Recomendados.**

| Parámetro             | Valor típico              |
|-----------------------|---------------------------|
| Capas ocultas         | 1 a 3                     |
| Neuronas por capa     | 16, 32 o 64               |
| Activación oculta     | ReLU                      |
| Activación salida     | Sigmoid                   |
| Tasa de aprendizaje   | 0.001 (con Adam)          |
| Epochs                | 50–100 + EarlyStopping    |
| Batch size            | 32 o 64                   |

## **Recomendaciones Técnicas para Caso de Uso.**

Dado que el proyecto consiste en predecir la supervivencia de pacientes a partir de datos clínicos estructurados y heterogéneos, se recomienda lo siguiente:

1. **Arquitectura del modelo**: utilizar un MLP con 2 capas ocultas (32 y 16 neuronas) con activación ReLU y una capa de salida sigmoidea.

2. **Preprocesamiento**:
   - One-oHt encoding para variables categóricas con múltiples valores.
   - Normalización (por ejemplo, MinMaxScaler) para bioquímicos y económicos.
   - Imputación de nulos con media/moda según el tipo de variable.

3. **Función de pérdida**: `binary_crossentropy`.

4. **Optimizador**: `Adam` con `learning_rate=0.001`.

5. **Regularización**: activar `Dropout` (por ejemplo, 0.3) en cada capa oculta y `EarlyStopping`.

6. **Evaluación**: aplicar validación cruzada con estratificación y reportar AUC-ROC, F1-score y matriz de confusión.

7. **Balanceo de clases**: si se detecta desbalance, usar `SMOTE` antes del entrenamiento.
