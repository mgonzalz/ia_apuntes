/*OBJETIVO:
Obtención de información de las tablas utilizadas en el Caso de Uso Redes Neuronales:
Diseñar, entrenar y evaluar un modelo de red neuronal que prediga la supervivencia de un paciente (vive = 1) a partir
de datos clínicos, genéticos, bioquímicos, sociodemográficos y económicos integrados.
*/
SELECT *
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'DATAEX' AND TABLE_NAME IN (
    'MONGO01_Bioquimicos',
    'MONGO02_Clinicos',
    'MONGO03_Geneticos',
    'MONGO04_Economicos',
    'MONGO05_Generales',
    'MONGO06_Sociodemograficos'
);

/*CONSULTAS OPCIONALES:
Obtener los datos completos de cada tabla
*/
-- SELECT * FROM DATAEX.MONGO01_Bioquimicos; -- Valores bioquímicos como glucosa, colesterol y creatinina.
-- SELECT * FROM DATAEX.MONGO02_Clinicos; -- Enfermedades diagnosticadas como diabetes, hipertensión o cáncer.
-- SELECT * FROM DATAEX.MONGO03_Geneticos; -- Mutaciones en genes relevantes como BRCA1, TP53 o EGFR.
-- SELECT * FROM DATAEX.MONGO04_Economicos; -- Datos económicos como ingresos, empleo y seguro médico.
-- SELECT * FROM DATAEX.MONGO05_Generales; -- Estilo de vida (fumador, alcohol, actividad física) y etiqueta de supervivencia.
-- SELECT * FROM DATAEX.MONGO06_Sociodemograficos; -- Edad, sexo, estado civil, educación y lugar de residencia.
