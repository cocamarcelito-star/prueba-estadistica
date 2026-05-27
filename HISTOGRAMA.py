import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# titulo
st.title("HISTOGRAMA")

# leer csv
df_est = pd.read_csv("estudiante.csv")

# edades
edades = df_est["edad"]

# intervalos
bins = [18,19.5,21,22.5,24,25.5,27]

# figura
plt.figure(figsize=(10,6))

# histograma
fi, clases, patches = plt.hist(
    edades,
    bins=bins,
    color='turquoise',
    edgecolor='white',
    alpha=0.7,
    label='Histograma'
)

# marcas de clase
xi = []

for i in range(len(clases)-1):
    xi.append((clases[i] + clases[i+1]) / 2)

# poligono
plt.plot(
    xi,
    fi,
    color='red',
    marker='D',
    linewidth=2,
    label='Polígono'
)

# titulo
plt.title(
    "ANÁLISIS DE DISTRIBUCIÓN DE EDADES",
    fontsize=16,
    fontweight='bold'
)

# ejes
plt.xlabel("Intervalos de Clase")
plt.ylabel("Frecuencia Absoluta (fi)")

# leyenda
plt.legend()

# cuadricula
plt.grid(True, alpha=0.4)

# mostrar
st.pyplot(plt)