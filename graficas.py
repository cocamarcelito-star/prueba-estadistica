import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# TITULO
# ==========================================
st.title("GRÁFICOS ESTADÍSTICOS")

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
# GRAFICO DE BASTON
# ==========================================
st.header("GRÁFICO DE BASTÓN")

frec_discreta = df_est["materias_aprobadas"].value_counts().sort_index()

fig1, ax1 = plt.subplots(figsize=(10,5))

markerline, stemlines, baseline = ax1.stem(
    frec_discreta.index,
    frec_discreta.values
)

plt.setp(stemlines, color='darkblue', linewidth=2)

plt.setp(
    markerline,
    marker='o',
    markersize=7,
    markerfacecolor='red',
    markeredgecolor='red'
)

plt.setp(baseline, visible=False)

ax1.set_title("AVANCE ACADÉMICO")
ax1.set_xlabel("Materias Aprobadas")
ax1.set_ylabel("Frecuencia")
ax1.grid(True)

st.pyplot(fig1)

# ==========================================
# HISTOGRAMA
# ==========================================
st.header("HISTOGRAMA")

edades = df_est["edad"]

bins = [18, 19.5, 21, 22.5, 24, 25.5, 27]

fig2, ax2 = plt.subplots(figsize=(10,5))

fi, clases, patches = ax2.hist(
    edades,
    bins=bins,
    color='turquoise',
    edgecolor='white',
    alpha=0.7
)

xi = []

for i in range(len(clases)-1):
    xi.append((clases[i] + clases[i+1]) / 2)

ax2.plot(
    xi,
    fi,
    color='red',
    marker='D',
    linewidth=2
)

ax2.set_title("ANÁLISIS DE EDADES")
ax2.set_xlabel("Intervalos")
ax2.set_ylabel("Frecuencia")
ax2.grid(True)

st.pyplot(fig2)

# ==========================================
# OJIVA
# ==========================================
st.header("OJIVA")

fi_ojiva = pd.cut(edades, bins=bins).value_counts().sort_index()

Fi = fi_ojiva.cumsum()

x = bins[1:]

fig3, ax3 = plt.subplots(figsize=(10,5))

ax3.plot(
    x,
    Fi,
    color='red',
    marker='s',
    linewidth=2
)

ax3.fill_between(x, Fi, color='purple', alpha=0.3)

ax3.set_title("OJIVA")
ax3.set_xlabel("Límites Superiores")
ax3.set_ylabel("Frecuencia Acumulada")
ax3.grid(True)

st.pyplot(fig3)

# ==========================================
# GRAFICO DE TORTA
# ==========================================
st.header("GRÁFICO DE TORTA")

carreras = df_est["carrera"].value_counts()

fig4, ax4 = plt.subplots(figsize=(8,8))

ax4.pie(
    carreras,
    labels=carreras.index,
    autopct='%1.1f%%',
    startangle=90
)

ax4.set_title("PORCENTAJE DE ESTUDIANTES POR CARRERA")

st.pyplot(fig4)