# **Modelización del Tráfico Web y Atribución Publicitaria en Retail.**

## **Descripción general.**

El dataset consolidado integra información de:

- Tráfico web.
- Tráfico físico en tienda.
- Inversión publicitaria.
- Factores temporales.
- Segmentación por categorías.

La clave común es `ID_Date`, que representa el mes del año en formato `YYYYMM`.

## **Información Datasets Disponibles.**

### **Web: Tráfico Digital.**

| Columna                         | Descripción                                                      |
|---------------------------------|------------------------------------------------------------------|
| `ID_Date`                       | Fecha en formato `YYYYMM`                                        |
| `Unique_visitors`              | Número total de visitantes únicos al sitio web (Interacción)                   |
| `PDFBrochuresDownloaded`       | Descargas de catálogos PDF (Interacción)                                      |
| `ProductConfigurator`          | Número de veces que se utilizó el configurador de productos (Interacción)        |
| `Product_configurator_Visists`| Visitas que usaron el configurador  (Interacción)                            |
| `SocialNetworks`               | Visitas desde redes sociales (Fuente Tráfico)                                    |
| `DirectTraffic`                | Tráfico directo al sitio web (Fuente Tráfico)                                 |
| `EMail`                        | Visitas desde campañas de email (Fuente Tráfico)                    |
| `NaturalSearch`                | Visitas desde búsquedas orgánicas (Fuente Tráfico)                 |
| `OnlineMedia`                  | Tráfico desde medios online (Fuente Tráfico)                    |
| `OtherReferrer`                | Referencias desde otras webs (Fuente Tráfico)                     |
| `PaidSearch`                   | Visitas desde búsquedas pagadas (SEM)                            |

### **Visit: Web por categoría.**

| Columna         | Descripción                                 |
|-----------------|---------------------------------------------|
| `RopaHombre`    | Visitas a productos de ropa para hombre     |
| `RopaMujer`     | Visitas a productos de ropa para mujer      |
| `Complementos`  | Visitas a accesorios de moda                |
| `Zapatos`       | Visitas a productos de calzado              |
| `Home`          | Visitas a productos de hogar                |
| `Interior`      | Visitas a productos de ropa interior        |
| `Otros`         | Visitas a productos que no entran en las categorías anteriores  |
| `SR_Total`      | Total de visitas web sumando todas las categorías    |

### **Offline: Tráfico físico y ventas.**

| Columna          | Descripción                                                 |
|------------------|-------------------------------------------------------------|
| `Visit_Store`    | Número de personas que ingresan a la tienda física                         |
| `Mercado`        | Ingresos monetarios totales generados por el canal físico   |
| `Sales`          |  Cantidad de transacciones realizadas en tienda                         |
| `Complementos` | Ventas de complementos (offline)                              |
| `Ropa_hombre`    | Ventas de ropa para hombre                                  |
| `Zapatos`      | Ventas de calzado                                             |
| `Ropa_Mujer`     | Ventas de ropa para mujer                                   |
| `Home`         | Ventas de productos de hogar                                  |
| `Interior`     | Ventas de ropa interior                                       |
| `Otros`        | Ventas de productos sin categoría definida                    |
| `Ticket_medio`   | Valor promedio de compra por cliente                         |

### **Time: Factores temporales.**

| Columna             | Descripción                                       |
|---------------------|---------------------------------------------------|
| `Dias_mes`          | Número total de días del mes                      |
| `Dia_inicio_mes`    | Día de la semana en que comienza el mes           |
| `Dia_findemes`      | Día de la semana en que termina el mes            |
| `working_days`      | Días laborables del mes                           |
| `Dias_fines_semana` | Número de fines de semana                         |
| `Easterweek`        | 1 si es Semana Santa, 0 si no                     |

### **Inv: Inversión publicitaria.**

| Columna            | Descripción                                               |
|--------------------|-----------------------------------------------------------|
| `CINE`             | Inversión publicitaria en cine  (Tradicional)                       |
| `EXTERIOR`         | Publicidad en exterior (carteles, marquesinas, etc.) (Tradicional)   |
| `INTERNET`         | Inversión en medios digitales (Digital)                |
| `PRENSA`           | Inversión en prensa escrita (Tradicional)                       |
| `PRODUCCION`       | Costes de producción de materiales publicitarios (Otros)    |
| `RADIO`            | Inversión en radio (Tradicional)                         |
| `REVISTAS`         | Inversión en revistas (Tradicional)                   |
| `PlataformasVideo` | Inversión en plataformas de video (YouTube, etc.) (Digital)     |
| `VARIOS`           | Otros gastos publicitarios diversos (Otros)             |
| `INV_Total`        | Inversión total mensual en publicidad               |
