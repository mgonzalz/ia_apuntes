import pandas as pd

class DataPreprocessor:
    """
    Clase para el preprocesamiento de datos antes de aplicar el modelo.
    Incluye:
    - Eliminación de valores duplicados.
    - Eliminación de valores nulos en columnas clave.
    - Relleno de valores faltantes en variables categóricas.
    - Detección y eliminación de outliers con IQR.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def remove_duplicates(self): # Elinación de filas duplicadas.
        duplicates_count = self.df.duplicated().sum()
        if duplicates_count > 0:
            self.df.drop_duplicates(inplace=True)

    def clean_missing_values(self): # Tratamiento de valores nulos.
        self.df.dropna(subset=['Averia_grave'], inplace=True)
        self.df.dropna(subset=["ESTADO_CIVIL", "GENERO"], inplace=True)
        self.df["Zona_Renta"] = self.df["Zona_Renta"].fillna("Desconocida")

    def remove_outliers(self): # Eliminación de outliers a través del IQR.
        outliers = {}
        v_continuas = self.df.select_dtypes(include=['float64', 'int64']).columns

        for col in v_continuas:
            Q1 = self.df[col].quantile(0.20)
            Q3 = self.df[col].quantile(0.80)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers[col] = self.df[(self.df[col] < lower_bound) | (self.df[col] > upper_bound)][col].count()
            self.df = self.df[(self.df[col] >= lower_bound) & (self.df[col] <= upper_bound)]

    def preprocess(self): # Ejecución de todo el proceso de preprocesamiento.
        self.remove_duplicates()
        self.clean_missing_values()
        self.remove_outliers()
        return self.df
