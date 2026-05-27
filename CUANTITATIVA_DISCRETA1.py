import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# titulo streamlit
st.title("CUANTITATIVA DISCRETA1")

# leer archivo csv
df_est = pd.read_csv("estudiante.csv")

# mostrar datos
st.subheader("DATOS DEL CSV")
st.write(df_est.head())

# ==========================================
# TABLA DE FRECUENCIAS
# ==========================================

# conteo de frecuencias
frec_discreta = df_est["materias_aprobadas"] \
    .value_counts() \
    .sort_index() \
    .reset_index()

# renombrar columnas
frec_discreta.columns = ["materias_aprobadas", "fi"]

# frecuencia relativa
frec_discreta["hi"] = frec_discreta["fi"] / len(df_est)

# frecuencia porcentual
frec_discreta["hip"] = frec_discreta["hi"] * 100

# frecuencia acumulada
frec_discreta["Fi"] = frec_discreta["fi"].cumsum()

# frecuencia relativa acumulada
frec_discreta["Hi"] = frec_discreta["hi"].cumsum()

# mostrar tabla
st.subheader("TABLA DE FRECUENCIAS")
st.write(frec_discreta)