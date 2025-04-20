/*OBJETIVO:
Unión completa de todas las tablas del caso de uso Marketing Mix Modeling
(MMM) mediante la clave común ID_Date. Esta vista consolidada permite
análisis cruzados entre tráfico online, tráfico físico, eventos temporales
e inversión publicitaria para modelos de atribución y forecasting.
*/
SELECT
    W.ID_Date,
    W.Unique_visitors,
    W.PDFBrochuresDownloaded,
    W.ProductConfigurator,
    W.Product_configurator_Visists,
    W.SocialNetworks,
    W.DirectTraffic,
    W.EMail,
    W.NaturalSearch,
    W.OnlineMedia,
    W.OtherReferrer,
    W.PaidSearch,
    V.RopaHombre,
    V.RopaMujer,
    V.Complementos,
    V.Zapatos,
    V.Home,
    V.Interior,
    V.Otros,
    V.SR_Total,
    O.Visit_Store,
    O.Mercado,
    O.Sales,
    O.Complementos,
    O.Ropa_hombre,
    O.Zapatos,
    O.Ropa_Mujer,
    O.Home,
    O.Interior,
    O.Otros,
    O.Ticket_medio,
    T.Dias_mes,
    T.Dia_inicio_mes,
    T.Dia_findemes,
    T.working_days,
    T.Dias_fines_semana,
    T.Easterweek,
    I.CINE,
    I.EXTERIOR,
    I.INTERNET,
    I.PRENSA,
    I.PRODUCCION,
    I.RADIO,
    I.REVISTAS,
    I.PlataformasVideo,
    I.VARIOS,
    I.INV_Total

FROM [usecases].DATAEX.[MMM01_WEB] W
JOIN [usecases].DATAEX.[MMM02_VISIT] V ON W.ID_Date = V.ID_Date
JOIN [usecases].DATAEX.[MMM03_OFFLINE] O ON W.ID_Date = O.ID_Date
JOIN [usecases].DATAEX.[MMM04_TIME] T ON W.ID_Date = T.ID_Date
JOIN [usecases].DATAEX.[MMM05_INV] I ON W.ID_Date = I.ID_Date
