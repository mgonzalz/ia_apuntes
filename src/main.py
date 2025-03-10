import os
import sys
import pandas as pd
from data_preprocessor import DataPreprocessor
from data_feature_engineering import FeatureEngineering

# Definición de las rutas de archivos.
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Rutas de los archivos de datos.
RAW_DATA_PATH = os.path.join(BASE_DIR, "data/raw/IA_PROPENSITY_INPUT.csv")
CLEANED_DATA_PATH = os.path.join(BASE_DIR, "data/cleaned/IA_PROPENSITY_INPUT.csv")
TRANSFORMED_DATA_PATH = os.path.join(BASE_DIR, "data/processed/IA_PROPENSITY_INPUT.csv")

def main():
    print("Iniciando pipeline de datos...")

    # Carga de datos.
    if not os.path.exists(RAW_DATA_PATH):
        print(f"ERROR: Archivo no encontrado: {RAW_DATA_PATH}")
        return
    df = pd.read_csv(RAW_DATA_PATH, index_col=0)
    print("1. Datos cargados correctamente.")

    # Preprocesamiento.
    preprocessor = DataPreprocessor(df)
    df_cleaned = preprocessor.preprocess()
    df_cleaned.to_csv(CLEANED_DATA_PATH, index=True)
    print(f"2. Datos preprocesados guardados en {CLEANED_DATA_PATH}")

    # Feature Engineering.
    fe = FeatureEngineering(df_cleaned)
    df_transformed = fe.transform()
    df_transformed.to_csv(TRANSFORMED_DATA_PATH, index=True)
    print(f"Feature Engineering completado y guardado en {TRANSFORMED_DATA_PATH}")

    print("Pipeline de datos finalizado con éxito.")

if __name__ == "__main__":
    main()
