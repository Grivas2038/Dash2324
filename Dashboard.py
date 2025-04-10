# %%
import streamlit as st
import pandas as pd
import plotly.express as px

# Leer los datos del archivo Excel
df = pd.read_excel("Marzo 2025.xlsx")

# Crear un gráfico interactivo con Plotly
fig = px.bar(df, x="Motivo del contacto", y="Nº", title="Contactos por Motivo")

# Configurar la aplicación con Streamlit
st.title("Test ID 2425")
st.plotly_chart(fig, use_container_width=True)
# %%
