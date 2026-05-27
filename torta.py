import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# titulo app
st.title("torta")

# leer csv
df_est = pd.read_csv("estudiante.csv")

# mostrar datos
st.subheader("DATOS DEL CSV")
st.dataframe(df_est)

# contar carreras
carreras = df_est["carrera"].value_counts()

# crear figura
fig, ax = plt.subplots(figsize=(8,8))

# grafico circular
ax.pie(
    carreras,
    labels=carreras.index,
    autopct='%1.1f%%',
    startangle=90
)

# titulo grafico
ax.set_title(
    "PORCENTAJE DE ESTUDIANTES POR CARRERA",
    fontsize=16,
    fontweight='bold'
)

# mostrar grafico
st.pyplot(fig)