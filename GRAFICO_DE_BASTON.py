import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# titulo streamlit
st.title("GRAFICO DE BASTON")

# leer csv
df_est = pd.read_csv("estudiante.csv")

# tabla frecuencia
frec_discreta = df_est["materias_aprobadas"].value_counts().sort_index()

# tamaño figura
plt.figure(figsize=(12,6))

# grafico baston
markerline, stemlines, baseline = plt.stem(
    frec_discreta.index,
    frec_discreta.values
)

# estilos
plt.setp(stemlines, color='darkblue', linewidth=2)

plt.setp(
    markerline,
    marker='o',
    markersize=7,
    markerfacecolor='red',
    markeredgecolor='red'
)

plt.setp(baseline, visible=False)

# titulo
plt.title(
    "AVANCE ACADÉMICO(VARIABLES DISCRETAS)",
    fontsize=18,
    fontweight='bold'
)

# ejes
plt.xlabel("Número de Materias Aprobadas", fontsize=14)
plt.ylabel("Frecuencia Absoluta (fi)", fontsize=14)

# cuadricula
plt.grid(True, alpha=0.5)

# mostrar en streamlit
st.pyplot(plt)