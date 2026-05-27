import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# titulo
st.title("Tabla de Frecuencias Agrupadas")

# leer csv
df_est = pd.read_csv("estudiantes.csv")

# mostrar datos
st.subheader("Datos del CSV")
st.dataframe(df_est)

# cantidad datos
n = len(df_est)

# maximo y minimo
maximo = df_est["edad"].max()
minimo = df_est["edad"].min()

# rango
R = maximo - minimo

# sturges
k = int(1 + 3.322 * np.log10(n))

# crear clases automaticamente
clases = pd.cut(df_est["edad"], bins=k)

# tabla frecuencia
frec_agrupada = clases.value_counts().sort_index().reset_index()

# nombres columnas
frec_agrupada.columns = ["intervalo", "fi"]

# frecuencia relativa
frec_agrupada["hi"] = frec_agrupada["fi"] / n

# porcentaje
frec_agrupada["hip"] = frec_agrupada["hi"] * 100

# acumuladas
frec_agrupada["Fi"] = frec_agrupada["fi"].cumsum()

frec_agrupada["Hi"] = frec_agrupada["hi"].cumsum()

# mostrar tabla
st.subheader("TABLA DE FRECUENCIAS AGRUPADAS")
st.dataframe(frec_agrupada)