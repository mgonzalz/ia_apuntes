import streamlit as st
import pandas as pd
import pickle
import os
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import joblib
import plotly.express as px

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from data_preprocessor import DataPreprocessor
from data_feature_engineering import FeatureEngineering

def segmentar_cliente(prob):
    if prob > 0.8:
        return "Premium"
    elif 0.8 >= prob > 0.6:
        return "Potencial"
    elif 0.6 >= prob > 0.15:
        return "Intermedio"
    else:
        return "Baja Propensión"

# Configuración de la app
st.set_page_config(layout="wide")
st.title("Segmentación de Clientes basada en Propensión de Compra")
st.sidebar.header("Carga de Datos")

# Cargar archivo CSV
# Ruta del archivo de ejemplo
example_path = os.path.join("data", "raw", "IA_PROPENSITY_INPUT.csv")
# Opción para usar un archivo de ejemplo
use_example = st.sidebar.checkbox("Usar archivo de ejemplo")
# Cargar archivo CSV
uploaded_file = st.sidebar.file_uploader("Sube un archivo CSV", type=["csv"])
# Inicializar df como None
df = None
if use_example:
    if os.path.exists(example_path):
        df = pd.read_csv(example_path, index_col=0)
        st.sidebar.success("Archivo de ejemplo cargado correctamente")
    else:
        st.sidebar.error(f"El archivo de ejemplo no se encontró en {example_path}.")
elif uploaded_file is not None:
    df = pd.read_csv(uploaded_file, index_col=0)
    st.sidebar.success("Archivo cargado correctamente")

# Cargar modelo XGBoost
model_path = os.path.join("models", "xgboost.pkl")
model = joblib.load(model_path)
expected_columns = model.get_booster().feature_names

if df is not None:
    st.sidebar.success("Archivo cargado correctamente")
    # Lista de columnas a eliminar si existen
    cols_to_drop = ['Mas_1_coche', 'Tiempo']

    # Verifica qué columnas de la lista están en el DataFrame
    cols_presentes = list(set(cols_to_drop) & set(df.columns))

    # Si hay columnas en la intersección, se eliminan
    if cols_presentes:
        df.drop(columns=cols_presentes, inplace=True)

    # Preprocesamiento de datos
    preprocessor = DataPreprocessor(df)
    df = preprocessor.preprocess()

    # Ingeniería de características
    feature_engineer = FeatureEngineering(df)
    df_modelo = feature_engineer.transform()

    # Predicciones de probabilidad.
    y_pred_proba = model.predict_proba(df_modelo)[:, 1]

    # Aplicación del umbral óptimo (según lo definido en el análisis anterior).
    umbral_optimo = 0.59
    y_pred = (y_pred_proba >= umbral_optimo).astype(int)
    df["Probabilidad_Compra"] = y_pred_proba
    df["Prediccion_Compra"] = y_pred
    df["Segmento"] = df["Probabilidad_Compra"].apply(segmentar_cliente)

    # Mostrar datos
    st.write("Vista previa de los datos procesados:")
    st.dataframe(df.head(6))
    st.write(f"**Proporción de clientes con Predicción de Compra:** {round(df['Probabilidad_Compra'].mean()*100, 2)}%")

    # Layout para dividir en dos columnas
    col1, col2 = st.columns([1,1])
    with col1:
        st.subheader("Distribución de Probabilidad de Compra por Segmento")
        plt.figure(figsize=(12,9))
        sns.histplot(data=df, x='Probabilidad_Compra', hue='Segmento', bins=30, kde=True)
        plt.xlabel("Probabilidad de Compra")
        plt.ylabel("Cantidad de Clientes")
        st.pyplot(plt)

    with col2:
        st.subheader("Distribución de Clientes por Segmento")
        segment_counts = df['Segmento'].value_counts().reset_index()
        segment_counts.columns = ['Segmento', 'Cantidad']
        fig_bar = px.bar(segment_counts, x='Segmento', y='Cantidad', text='Cantidad', title="Clientes por Segmento",
                         color='Segmento', color_discrete_map={
                             "Baja Propensión": "#E26768",
                             "Intermedio": "#FFA556",
                             "Potencial": "#629FCA",
                             "Premium": "#6BBC6B"
                         })
        fig_bar.update_traces(textposition='outside')
        st.plotly_chart(fig_bar, use_container_width=True)
    st.subheader("Simulación del Impacto Comercial:")
    col1, col2 = st.columns([2,2])
    with col1:
        conversion_rates = {
            "Premium": 0.93,
            "Potencial": 0.54,
            "Intermedio": 0.23,
            "Baja Propensión": 0.006
        }
        segment_counts["Clientes_Convertidos_NE"] = segment_counts["Segmento"].map(conversion_rates) * segment_counts["Cantidad"]
        fig_conversion = px.bar(segment_counts.melt(id_vars="Segmento", value_vars=["Cantidad", "Clientes_Convertidos_NE"]),
                                x="Segmento", y="value", color="variable", barmode="group",
                                title="Impacto de la Falta de Estrategia en la Conversión de Clientes",
                                color_discrete_map={"Cantidad": "#629FCA", "Clientes_Convertidos_NE": "#FFC300"})
        fig_conversion.update_layout(legend_title_text="Métrica")
        fig_conversion.for_each_trace(lambda t: t.update(name='Cliente Total' if t.name == 'Cantidad' else 'Do Nothing'))
        st.plotly_chart(fig_conversion, use_container_width=True)
    
    with col2:
        # Gráfico de impacto con estrategia
        conversion_rates_with_strategy = conversion_rates.copy()
        conversion_rates_with_strategy["Premium"] *= 1.05
        conversion_rates_with_strategy["Potencial"] *= 1.30
        conversion_rates_with_strategy["Intermedio"] *= 1.25
        conversion_rates_with_strategy["Baja Propensión"] *= 1.10
        segment_counts["Clientes_Convertidos"] = segment_counts["Segmento"].map(conversion_rates_with_strategy) * segment_counts["Cantidad"]
        
        fig_strategy = px.bar(segment_counts.melt(id_vars="Segmento", value_vars=["Clientes_Convertidos_NE", "Clientes_Convertidos"]),
                            x="Segmento", y="value", color="variable", barmode="group",
                            title="Impacto de la Estrategia en la Conversión de Clientes",
                            color_discrete_map={"Clientes_Convertidos_NE": "#FFC300", "Clientes_Convertidos": "#1F77B4"})
        fig_strategy.update_layout(legend_title_text="Estrategia")
        fig_strategy.for_each_trace(lambda t: t.update(name='Do Nothing' if t.name == 'Clientes_Convertidos_NE' else 'Do Something'))
        st.plotly_chart(fig_strategy, use_container_width=True)

    col1, col2 = st.columns([3, 3])

    # FILA 1: Baja Propensión vs Intermedio
    with col1:
        baja_propension = df[df['Segmento'] == 'Baja Propensión']
        st.subheader("Análisis de Clientes en Baja Propensión")
        c1, c2 = st.columns(2)

        fig_km = px.histogram(baja_propension, x="km_anno", nbins=20, labels={"km_anno": "Kilometraje Anual"}, color_discrete_sequence=["#1f77b4"])
        fig_km.update_layout(height=350, width=550)
        c1.plotly_chart(fig_km, use_container_width=True)

        fig_edad = px.scatter(baja_propension, x="Edad_Cliente", y="Probabilidad_Compra", labels={"Edad_Cliente": "Edad del Cliente", "Probabilidad_Compra": "Probabilidad de Compra"},
                            color_discrete_sequence=["#ff7f0e"], opacity=0.7)
        fig_edad.update_layout(height=350, width=550)
        c2.plotly_chart(fig_edad, use_container_width=True)

        c3, c4 = st.columns(2)

        fig_coste = px.histogram(baja_propension, x="COSTE_VENTA", nbins=20, labels={"COSTE_VENTA": "Coste de Venta"}, color_discrete_sequence=["#2ca02c"])
        fig_coste.update_layout(height=350, width=550)
        c3.plotly_chart(fig_coste, use_container_width=True)

        forma_pago_counts = baja_propension["FORMA_PAGO"].value_counts().reset_index()
        forma_pago_counts.columns = ["Forma de Pago", "Número de Clientes"]
        fig_pago = px.bar(forma_pago_counts, y="Forma de Pago", x="Número de Clientes", orientation="h", color_discrete_sequence=["#d62728"])
        fig_pago.update_layout(height=350, width=550)
        c4.plotly_chart(fig_pago, use_container_width=True)


    with col2:
        intermedio_propension = df[df["Segmento"] == "Intermedio"]
        st.subheader("Análisis de Clientes en Intermedio")
        c5, c6 = st.columns(2)

        fig_km_int = px.histogram(intermedio_propension, x="km_anno", nbins=20, labels={"km_anno": "Kilometraje Anual"}, color_discrete_sequence=["#1f77b4"])
        fig_km_int.update_layout(height=350, width=550)
        c5.plotly_chart(fig_km_int, use_container_width=True)

        fig_edad_int = px.scatter(intermedio_propension, x="Edad_Cliente", y="Probabilidad_Compra", labels={"Edad_Cliente": "Edad del Cliente", "Probabilidad_Compra": "Probabilidad de Compra"},
                                color_discrete_sequence=["#ff7f0e"], opacity=0.7)
        fig_edad_int.update_layout(height=350, width=550)
        c6.plotly_chart(fig_edad_int, use_container_width=True)

        c7, c8 = st.columns(2)

        fig_coste_int = px.histogram(intermedio_propension, x="COSTE_VENTA", nbins=20, labels={"COSTE_VENTA": "Coste de Venta"}, color_discrete_sequence=["#2ca02c"])
        fig_coste_int.update_layout(height=350, width=550)
        c7.plotly_chart(fig_coste_int, use_container_width=True)

        forma_pago_counts_int = intermedio_propension["FORMA_PAGO"].value_counts().reset_index()
        forma_pago_counts_int.columns = ["Forma de Pago", "Número de Clientes"]
        fig_pago_int = px.bar(forma_pago_counts_int, y="Forma de Pago", x="Número de Clientes", orientation="h", color_discrete_sequence=["#d62728"])
        fig_pago_int.update_layout(height=350, width=550)
        c8.plotly_chart(fig_pago_int, use_container_width=True)


    # FILA 2: Potencial vs Premium
    col3, col4 = st.columns([3, 3])

    with col3:
        potencial_propension = df[df["Segmento"] == "Potencial"]
        st.subheader("Análisis de Clientes en Potencial")
        c9, c10 = st.columns(2)

        fig_km_pot = px.histogram(potencial_propension, x="km_anno", nbins=20, labels={"km_anno": "Kilometraje Anual"}, color_discrete_sequence=["#1f77b4"])
        fig_km_pot.update_layout(height=350, width=550)
        c9.plotly_chart(fig_km_pot, use_container_width=True)

        fig_edad_pot = px.scatter(potencial_propension, x="Edad_Cliente", y="Probabilidad_Compra", labels={"Edad_Cliente": "Edad del Cliente", "Probabilidad_Compra": "Probabilidad de Compra"},
                                color_discrete_sequence=["#ff7f0e"], opacity=0.7)
        fig_edad_pot.update_layout(height=350, width=550)
        c10.plotly_chart(fig_edad_pot, use_container_width=True)

        c11, c12 = st.columns(2)

        fig_coste_pot = px.histogram(potencial_propension, x="COSTE_VENTA", nbins=20, labels={"COSTE_VENTA": "Coste de Venta"}, color_discrete_sequence=["#2ca02c"])
        fig_coste_pot.update_layout(height=350, width=550)
        c11.plotly_chart(fig_coste_pot, use_container_width=True)

        forma_pago_counts_pot = potencial_propension["FORMA_PAGO"].value_counts().reset_index()
        forma_pago_counts_pot.columns = ["Forma de Pago", "Número de Clientes"]
        fig_pago_pot = px.bar(forma_pago_counts_pot, y="Forma de Pago", x="Número de Clientes", orientation="h", color_discrete_sequence=["#d62728"])
        fig_pago_pot.update_layout(height=350, width=550)
        c12.plotly_chart(fig_pago_pot, use_container_width=True)


    with col4:
        premium_propension = df[df["Segmento"] == "Premium"]
        st.subheader("Análisis de Clientes en Premium")
        c13, c14 = st.columns(2)

        fig_km_prem = px.histogram(premium_propension, x="km_anno", nbins=20, labels={"km_anno": "Kilometraje Anual"}, color_discrete_sequence=["#1f77b4"])
        fig_km_prem.update_layout(height=350, width=550)
        c13.plotly_chart(fig_km_prem, use_container_width=True)

        fig_edad_prem = px.scatter(premium_propension, x="Edad_Cliente", y="Probabilidad_Compra", labels={"Edad_Cliente": "Edad del Cliente", "Probabilidad_Compra": "Probabilidad de Compra"},
                                    color_discrete_sequence=["#ff7f0e"], opacity=0.7)
        fig_edad_prem.update_layout(height=350, width=550)
        c14.plotly_chart(fig_edad_prem, use_container_width=True)

        c15, c16 = st.columns(2)

        fig_coste_prem = px.histogram(premium_propension, x="COSTE_VENTA", nbins=20, labels={"COSTE_VENTA": "Coste de Venta"}, color_discrete_sequence=["#2ca02c"])
        fig_coste_prem.update_layout(height=350, width=550)
        c15.plotly_chart(fig_coste_prem, use_container_width=True)

        forma_pago_counts_prem = premium_propension["FORMA_PAGO"].value_counts().reset_index()
        forma_pago_counts_prem.columns = ["Forma de Pago", "Número de Clientes"]
        fig_pago_prem = px.bar(forma_pago_counts_prem, y="Forma de Pago", x="Número de Clientes", orientation="h", color_discrete_sequence=["#d62728"])
        fig_pago_prem.update_layout(height=350, width=550)
        c16.plotly_chart(fig_pago_prem, use_container_width=True)


    # Descargar resultados
    csv = df.to_csv(index=True).encode('utf-8')
    st.download_button("Descargar Resultados", data=csv, file_name="segmentacion_clientes.csv", mime="text/csv")

# Predicción con parámetros individuales
st.sidebar.header("Predicción Personalizada")
producto = st.sidebar.selectbox("Producto", ['A', 'B', 'C', 'H', 'J', 'D', 'I', 'E', 'F', 'K', 'G'])
tipo_carroceria = st.sidebar.selectbox("Tipo de Carrocería", ['TIPO1', 'TIPO6', 'TIPO4', 'TIPO7', 'TIPO8', 'TIPO2', 'TIPO3', 'TIPO5'])
combustible = st.sidebar.selectbox("Combustible", ['FUEL 1', 'FUEL 2'])
potencia = st.sidebar.selectbox("Potencia", ['Baja', 'Media', 'Alta'])
trans = st.sidebar.selectbox("Transmisión", ['M', 'A'])
forma_pago = st.sidebar.selectbox("Forma de Pago", ['Contado', 'Otros', 'Financiera Marca', 'Financiera Banco'])
estado_civil = st.sidebar.selectbox("Estado Civil", ['CASADO', 'SOLTERO', 'OTROS', 'EN PAREJA'])
genero = st.sidebar.selectbox("Género", ['M', 'F'])
ocupacion = st.sidebar.selectbox("Ocupación", ['Empresa', 'Funcionario', 'Autonomo'])
provincia = st.sidebar.selectbox("Provincia", ['Asturias', 'Toledo', 'Lerida', 'Madrid', 'Santa Cruz de Tenerife', 'Pontevedra', 'Lacoruna', 'Barcelona', 'Cordoba', 'Guipuzcua', 'Valladolid', 'Castellon', 'Valencia', 'Las Palmas', 'La Rioja', 'Baleares', 'Zaragoza', 'Alicante', 'Tarragona', 'Leon', 'Lugo', 'Badajoz', 'Vizcaya', 'Sevilla', 'Guadalajara', 'Ciudad Real', 'Cantabria', 'Orense', 'Navarra', 'Gerona', 'Malaga', 'Jaen', 'Murcia', 'Burgos', 'Granada', 'Alava', 'Cuenca', 'Cadiz', 'Salamanca', 'Albacete', 'Almeria', 'Teruel', 'Segovia', 'Palencia', 'Huelva', 'Huesca', 'Zamora', 'Avila', 'Soria', 'Caceres', 'Melilla', 'Ceuta', 'Francia'])
coste_venta = st.sidebar.number_input("Coste Venta", min_value=0.0)
km_anno = st.sidebar.number_input("Kilómetros por Año", min_value=0.0)
revisiones = st.sidebar.number_input("Revisiones", min_value=0)
edad_cliente = st.sidebar.number_input("Edad Cliente", min_value=18)
zona_renta = st.sidebar.selectbox("Zona de Renta", ["Otros", "Medio-Bajo", "Medio", "Alto"])
averia_grave = st.sidebar.selectbox("Avería Grave", ["No", "Averia leve", "Averia grave", "Averia muy grave"])
campanna1 = st.sidebar.selectbox("Campaña 1", ["SI", "NO"])
campanna2 = st.sidebar.selectbox("Campaña 2", ["SI", "NO"])
campanna3 = st.sidebar.selectbox("Campaña 3", ["SI", "NO"])
queja_cac = st.sidebar.selectbox("Queja CAC", ["SI", "NO"])
rev_garantia = st.sidebar.selectbox("Revisión Garantía", ["SI", "NO DATA"])

if st.sidebar.button("Predecir Segmento"):
    input_data = pd.DataFrame([[producto, tipo_carroceria, combustible, potencia, trans, forma_pago, estado_civil, genero, ocupacion, provincia, coste_venta, km_anno, revisiones, edad_cliente, zona_renta, averia_grave, campanna1, campanna2, campanna3, queja_cac, rev_garantia]], 
                              columns=['PRODUCTO', 'TIPO_CARROCERIA', 'COMBUSTIBLE', 'Potencia', 'TRANS', 'FORMA_PAGO', 'ESTADO_CIVIL', 'GENERO', 'OcupaciOn', 'PROVINCIA', 'COSTE_VENTA', 'km_anno', 'Revisiones', 'Edad_Cliente', 'Zona_Renta', 'Averia_grave', 'Campanna1', 'Campanna2', 'Campanna3', 'QUEJA_CAC', 'REV_Garantia'])
    
    preprocessor = DataPreprocessor(input_data)
    input_data = preprocessor.preprocess()
    # Aplicar preprocesamiento e ingeniería de características
    input_data = FeatureEngineering(input_data).transform()
    input_data = input_data.reindex(columns=expected_columns, fill_value=0)
    
    # Hacer la predicción
    probabilidad = model.predict_proba(input_data)[:, 1][0]
    segmento = segmentar_cliente(probabilidad)
    
    st.write(f"Probabilidad de Compra: {probabilidad:.2f}")
    st.write(f"Segmento Asignado: {segmento}")
