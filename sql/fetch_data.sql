/*OBJETIVO:
Obtención de información de las tablas utilizadas en el Caso de Uso MMM (Marketing Mix Model)
para modelización de tráfico web y atribución de inversión publicitaria.
*/
SELECT *
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'DATAEX' AND TABLE_NAME IN (
    'MMM01_WEB',    -- Datos de tráfico web
    'MMM02_VISIT',  -- Visitas por categoría de producto
    'MMM03_OFFLINE',-- Visitas y ventas físicas en tienda
    'MMM04_TIME',   -- Datos temporales (festivos, eventos, etc.)
    'MMM05_INV'     -- Inversión publicitaria por canal
);

/*CONSULTAS OPCIONALES:
Obtener los datos completos de cada tabla
*/
-- SELECT * FROM DATAEX.MMM01_WEB;      -- Tráfico web
-- SELECT * FROM DATAEX.MMM02_VISIT;    -- Visitas por categoría
-- SELECT * FROM DATAEX.MMM03_OFFLINE;  -- Tráfico y ventas físicas
-- SELECT * FROM DATAEX.MMM04_TIME;     -- Variables temporales
-- SELECT * FROM DATAEX.MMM05_INV;      -- Inversión publicitaria
