import streamlit as st
import pandas as pd
import numpy as np

# ==========================================
# TITULO
# ==========================================
st.title("TABLAS DE FRECUENCIAS")

# ==========================================
# LEER CSV
# ==========================================
df_est = pd.read_csv("estudiante.csv")

# ==========================================
# MOSTRAR DATOS
# ==========================================
st.subheader("DATOS DEL CSV")
st.dataframe(df_est)

# ==========================================
# TABLA DE FRECUENCIA DISCRETA
# ==========================================
st.header("CUANTITATIVA DISCRETA")

frec_discreta = (
    df_est["materias_aprobadas"]
    .value_counts()
    .sort_index()
    .reset_index()
)

frec_discreta.columns = ["materias_aprobadas", "fi"]

frec_discreta["hi"] = frec_discreta["fi"] / len(df_est)
frec_discreta["hip"] = frec_discreta["hi"] * 100
frec_discreta["Fi"] = frec_discreta["fi"].cumsum()
frec_discreta["Hi"] = frec_discreta["hi"].cumsum()

st.subheader("Tabla de Frecuencias Discreta")
st.dataframe(frec_discreta)

# ==========================================
# TABLA DE FRECUENCIA CUALITATIVA
# ==========================================
st.header("VARIABLE CUALITATIVA")

frec_cualita = (
    df_est["carrera"]
    .value_counts()
    .reset_index()
)

frec_cualita.columns = ["carrera", "fi"]

frec_cualita["hi"] = frec_cualita["fi"] / len(df_est)
frec_cualita["hip"] = frec_cualita["hi"] * 100
frec_cualita["Fi"] = frec_cualita["fi"].cumsum()
frec_cualita["Hi"] = frec_cualita["hi"].cumsum()

st.subheader("Tabla de Frecuencias de Carrera")
st.dataframe(frec_cualita)

# ==========================================
# TABLA DE FRECUENCIA AGRUPADA
# ==========================================
st.header("CUANTITATIVA CONTINUA")

n = len(df_est)

maximo = df_est["edad"].max()
minimo = df_est["edad"].min()

R = maximo - minimo

k = int(1 + 3.322 * np.log10(n))

clases = pd.cut(df_est["edad"], bins=k)

frec_agrupada = (
    clases.value_counts()
    .sort_index()
    .reset_index()
)

frec_agrupada.columns = ["intervalo", "fi"]

# Convertir intervalos a texto
frec_agrupada["intervalo"] = frec_agrupada["intervalo"].apply(
    lambda x: f"{x.left:.1f} - {x.right:.1f}"
)

frec_agrupada["hi"] = frec_agrupada["fi"] / n
frec_agrupada["hip"] = frec_agrupada["hi"] * 100
frec_agrupada["Fi"] = frec_agrupada["fi"].cumsum()
frec_agrupada["Hi"] = frec_agrupada["hi"].cumsum()

st.subheader("Tabla de Frecuencias Agrupadas")
st.dataframe(frec_agrupada)

# ==========================================
# DATOS ESTADISTICOS
# ==========================================
st.subheader("DATOS ESTADÍSTICOS")

st.write("Número de datos (n):", n)
st.write("Valor mínimo:", minimo)
st.write("Valor máximo:", maximo)
st.write("Rango:", R)
st.write("Número de clases (k):", k)