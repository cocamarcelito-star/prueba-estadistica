import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# titulo
st.title("OJIVA")

# leer csv
df_est = pd.read_csv("estudiante.csv")

# edades
edades = df_est["edad"]

# intervalos
bins = [18,19.5,21,22.5,24,25.5,27]

# frecuencias
fi = pd.cut(edades, bins=bins).value_counts().sort_index()

# acumuladas
Fi = fi.cumsum()

# limites superiores
x = bins[1:]

# figura
plt.figure(figsize=(10,6))

# ojiva
plt.plot(
    x,
    Fi,
    color='red',
    marker='s',
    linewidth=2,
    label='Ojiva'
)

# sombreado
plt.fill_between(x, Fi, color='purple', alpha=0.3)

# titulo
plt.title(
    "ANÁLISIS DE DISTRIBUCIÓN DE EDADES",
    fontsize=16,
    fontweight='bold'
)

# ejes
plt.xlabel("Intervalos de Clase")
plt.ylabel("Frecuencia Acumulada (Fi)")

# leyenda
plt.legend()

# cuadricula
plt.grid(True, alpha=0.4)

# mostrar
st.pyplot(plt)