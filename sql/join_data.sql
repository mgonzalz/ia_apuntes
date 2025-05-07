SELECT
    soc.paciente_id,

    -- 01 - Bioquímicos.
    bio.glucosa, bio.colesterol, bio.trigliceridos, bio.hemoglobina,
    bio.leucocitos, bio.plaquetas, bio.creatinina,

    -- 02 - Clínicos.
    cli.diabetes, cli.hipertension, cli.obesidad, cli.cancer,
    cli.enfermedad_cardiaca, cli.asma, cli.epoc,

    -- 03 - Genéticos.
    mut.mut_BRCA1, mut.mut_TP53, mut.mut_EGFR, mut.mut_KRAS,
    mut.mut_PIK3CA, mut.mut_ALK, mut.mut_BRAF,

    -- 04 - Económicos.
    eco.ingresos_mensuales, eco.gastos_salud, eco.seguro_salud,
    eco.deudas, eco.tipo_empleo, eco.ayudas_publicas,

    -- 05 - Generales: Incluye la variable objetivo.
    gen.fumador, gen.alcohol, gen.actividad_fisica, gen.vive,

    -- 06 - Sociodemográficos.
    soc.edad, soc.sexo, soc.estado_civil, soc.nivel_educativo, soc.ocupacion,
    soc.region, soc.pais_nacimiento, soc.codigo_postal

FROM DATAEX.MONGO06_Sociodemograficos AS soc
INNER JOIN DATAEX.MONGO05_Generales AS gen
    ON soc.paciente_id = gen.paciente_id
INNER JOIN DATAEX.MONGO02_Clinicos AS cli
    ON soc.paciente_id = cli.paciente_id
INNER JOIN DATAEX.MONGO01_Bioquimicos AS bio
    ON soc.paciente_id = bio.paciente_id
INNER JOIN DATAEX.MONGO03_Geneticos AS mut
    ON soc.paciente_id = mut.paciente_id
INNER JOIN DATAEX.MONGO04_Economicos AS eco
    ON soc.paciente_id = eco.paciente_id;
