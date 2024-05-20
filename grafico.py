import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('netflix_titles.csv', encoding='latin-1')

title_types = df['type'].value_counts()

fig, ax = plt.subplots(figsize=(10, 6))  # Definir tamanho do gráfico
title_types.plot(kind='pie', color=['blue', 'pink'], ax=ax)
ax.set_xlabel('Tipo de Título')
ax.set_ylabel('Contagem')
ax.set_title('Contagem de Títulos na Netflix por Tipo')
ax.tick_params(axis='x', rotation=0)

st.pyplot(fig)
