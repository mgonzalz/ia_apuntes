import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, LabelEncoder

class FeatureEngineering:
    """
    Clase para realizar ingeniería de características en los datos.
    Incluye:
    - Clasificación de variables continuas y categóricas.
    - Codificación de variables categóricas.
    - Transformaciones de variables ordinales.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        self.v_continuas = []
        self.v_categoricas = []

    def classify_variables(self): # Clasificación de variables categóricas y continuas.
        for col in self.df.columns:
            if self.df[col].nunique() > 55 or self.df[col].dtype in ['float64', 'int64']:
                self.v_continuas.append(col)
            else:
                self.v_categoricas.append(col)

    def map_variables(self): # Mapeo de variables categóricas.
        # Asignación de la comunidad autónoma a cada provincia.
        region_dict = {
            "Andalucia": ["Almeria", "Cadiz", "Cordoba", "Granada", "Huelva", "Jaen", "Malaga", "Sevilla"],
            "Aragon": ["Huesca", "Teruel", "Zaragoza"],
            "Asturias": ["Asturias"],
            "Baleares": ["Baleares"],
            "Canarias": ["Las Palmas", "Santa Cruz de Tenerife"],
            "Cantabria": ["Cantabria"],
            "Castilla y Leon": ["Avila", "Burgos", "Leon", "Palencia", "Salamanca", "Segovia", "Soria", "Valladolid", "Zamora"],
            "Castilla La Mancha": ["Albacete", "Ciudad Real", "Cuenca", "Guadalajara", "Toledo"],
            "Cataluña": ["Barcelona", "Gerona", "Lerida", "Tarragona"],
            "Extremadura": ["Badajoz", "Caceres"],
            "Galicia": ["Coruña", "Lugo", "Orense", "Pontevedra", "Lacoruna"],
            "Madrid": ["Madrid"],
            "Murcia": ["Murcia"],
            "Navarra": ["Navarra"],
            "Pais Vasco": ["Alava", "Guipuzcua", "Vizcaya"],
            "La Rioja": ["La Rioja"],
            "Valencia": ["Alicante", "Castellon", "Valencia"],
            "Ceuta y Melilla": ["Ceuta", "Melilla"]
        }

        self.df["COMUNIDAD_AUT"] = self.df["PROVINCIA"].apply(lambda x: next((reg for reg, provs in region_dict.items() if x in provs), None))
        self.df = self.df[self.df['PROVINCIA'] != 'Francia']  # Filtrar solo España.
        self.df.drop(columns=["PROVINCIA"], inplace=True)
        self.v_categoricas = [col for col in self.v_categoricas if col != "PROVINCIA" and self.df[col].dtype != "float64"]
        self.v_categoricas.append("COMUNIDAD_AUT")

        # Mapeo de la variable Forma de Pago.
        self.df['FORMA_PAGO'] = self.df['FORMA_PAGO'].replace({
            'Financiera Marca': 'Financiado',
            'Financiera Banco': 'Financiado'
        })

    def encode_variables(self): # Codificación de variables categóricas y ordinales.
        # Codificación de variables ordinales.
        ordinal_cols = {
            "Potencia": ["Baja", "Media", "Alta"],
            "Zona_Renta": ["Desconocida", "Otros", "Medio-Bajo", "Medio", "Alto"],
            "Averia_grave": ["No", "Averia leve", "Averia grave", "Averia muy grave"]
        }
        ordinal_encoder = OrdinalEncoder(categories=[ordinal_cols[col] for col in ordinal_cols])
        self.df[list(ordinal_cols.keys())] = ordinal_encoder.fit_transform(self.df[list(ordinal_cols.keys())])

        # Codificación de variables nominales.
        label_cols = [col for col in self.v_categoricas if self.df[col].dtype != "float64"]
        for col in label_cols:
            le = LabelEncoder()
            self.df[col] = le.fit_transform(self.df[col])

    def bin_continuous_variables(self): # Agrupación de variables continuas.
        self.df['Edad_Cliente'] = pd.cut(self.df['Edad_Cliente'], bins=[17, 30, 50, 71], labels=['18-30', '31-50', '51+'])
        self.df['Revisiones'] = pd.cut(self.df['Revisiones'], bins=[-1, 0, 2, 4, 13], labels=['0', '1-2', '3-4', '5+'])
        for col in ['Revisiones', 'Edad_Cliente']:
            le = LabelEncoder()
            self.df[col] = le.fit_transform(self.df[col])
    
    def transform(self): # Aplicar todas las transformaciones.
        self.classify_variables()
        self.map_variables()
        self.encode_variables()
        self.bin_continuous_variables()
        return self.df
