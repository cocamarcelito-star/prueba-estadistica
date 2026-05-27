import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# titulo streamlit
st.title("GRAFICO DE BARRAS")

# leer archivo csv
df_est = pd.read_csv("estudiantes.csv")

# mostrar primeras filas
st.subheader("DATOS DEL CSV")
st.write(df_est.head())

# frecuencia de carreras
frec_cualita = df_est["carrera"].value_counts().reset_index()

# renombrar columnas
frec_cualita.columns = ["carrera", "fi"]

# frecuencia relativa
frec_cualita["hi"] = frec_cualita["fi"] / len(df_est)

# porcentaje
frec_cualita["hip"] = frec_cualita["hi"] * 100

# frecuencia acumulada
frec_cualita["Fi"] = frec_cualita["fi"].cumsum()

# frecuencia relativa acumulada
frec_cualita["Hi"] = frec_cualita["hi"].cumsum()

# mostrar tabla
st.subheader("TABLA DE FRECUENCIAS")
st.write(frec_cualita)

# tamaño grafico
plt.figure(figsize=(8,5))

# grafico barras
plt.bar(
    frec_cualita["carrera"],
    frec_cualita["fi"]
)

# titulo
plt.title("Frecuencia de Carreras")

# ejes
plt.xlabel("Carreras")
plt.ylabel("Frecuencia")

# cuadricula
plt.grid(True)

# mostrar grafico en streamlit
st.pyplot(plt)