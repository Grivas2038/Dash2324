# %%
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_excel("Marzo 2025.xlsx")

fig = px.bar(df, x="Motivo del contacto", y="Nº", title="Contactos por Motivo")

st.write(df.head())

st.title("Test ID 2425")

st.plotly_chart(fig, use_container_width=True)
