import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('netflix_titles.csv', encoding='latin-1')
title_types = df['type'].value_counts()

fig1, ax1 = plt.subplots(figsize=(10, 6))

title_types.plot(kind='pie', colors=['blue', 'pink'], ax=ax)
ax1.set_ylabel('')  # Remover o rótulo do eixo Y
ax1.set_title('Contagem de Títulos na Netflix por Tipo')
ax1.tick_params(axis='x', rotation=0)
st.pyplot(fig1)

title_types = df['type'].value_counts()

fig2, ax2 = plt.subplots(figsize=(10, 6))

title_types.plot(kind='bars', colors=['blue', 'pink'], ax=ax)
ax2.set_ylabel('')  # Remover o rótulo do eixo Y
ax2.set_title('Contagem de Títulos na Netflix por Tipo')
ax2.tick_params(axis='x', rotation=0)
st.pyplot(fig2)
