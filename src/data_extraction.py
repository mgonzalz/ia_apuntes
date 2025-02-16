import pyodbc
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv() # Cargar variables de entorno desde .env

# Configuración segura de conexión a Azure SQL.
SERVER = os.getenv("SERVER")
DATABASE = os.getenv("DATABASE")
DRIVER = os.getenv("DRIVER")

# Usar autenticación interactiva de Azure Active Directory.
conn_str = f"DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};Authentication=ActiveDirectoryInteractive"

try:
    # Conexión a Azure SQL.
    conn = pyodbc.connect(conn_str)
    sql_query = "SELECT * FROM [DATAEX].[IA_PROPENSITY_TRAIN]"
    data = pd.read_sql(sql_query, conn)
    print("Conexión exitosa con Azure SQL usando AAD.")

    # Ruta de datos exportados.
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "raw"))
    csv_path = os.path.join(base_dir, "IA_PROPENSITY_TRAIN.csv")
    data.to_csv(csv_path, index=False, encoding='utf-8-sig')
    print(f" Datos exportados exitosamente a: {csv_path}")

except Exception as e:
    print(f" Error de conexión: {e}")
