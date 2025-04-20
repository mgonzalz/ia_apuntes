import pyodbc
import pandas as pd
import os
import warnings

# Desactivar advertencias.
warnings.filterwarnings("ignore", category=UserWarning)

# Configuración de conexión a Azure SQL.
SERVER = os.getenv("SERVER", "")
DATABASE = os.getenv("DATABASE", "")
DRIVER = os.getenv("DRIVER", "{ODBC Driver 17 for SQL Server}")

# Cadena de conexión AAD.
conn_str = f"DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};Authentication=ActiveDirectoryInteractive"

# Tablas a descargar.
tables = [
    "MMM01_WEB",      # Tráfico web.
    "MMM02_VISIT",    # Visitas por categoría.
    "MMM03_OFFLINE",  # Tráfico y ventas físicas.
    "MMM04_TIME",     # Factores temporales.
    "MMM05_INV"       # Inversión publicitaria.
]

# Descarga de datos de Azure SQL.
try:
    # Conexión a Azure SQL.
    conn = pyodbc.connect(conn_str)
    print("Conexión exitosa con Azure SQL usando AAD.")

    # Ruta para guardar los datos.
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
    os.makedirs(base_dir, exist_ok=True)

    # Descargar y guardar cada tabla.
    for table in tables:
        print(f"Descargando datos de {table}...")
        sql_query = f"SELECT * FROM [DATAEX].[{table}]"
        df = pd.read_sql(sql_query, conn)

        # Guardar CSV.
        csv_path = os.path.join(base_dir, f"{table}.csv")
        df.to_csv(csv_path, index=False, encoding='utf-8-sig')
        print(f"- Datos exportados a: {csv_path}")

    print("Todas las tablas han sido descargadas correctamente.")

except Exception as e:
    print(f"Error de conexión o descarga: {e}")
