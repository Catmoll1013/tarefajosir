

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv('netflix_titles.csv', encoding='latin-1')

# Gráfico 1: Contagem de tipos de título
title_types = df['type'].value_counts()
fig1, ax1 = plt.subplots(figsize=(8, 6))
title_types.plot(kind='bar', color=['blue', 'pink'], ax=ax1)
ax1.set_xlabel('Tipo de Título')
ax1.set_ylabel('Contagem')
ax1.set_title('Contagem de Títulos na Netflix por Tipo')
ax1.tick_params(axis='x', rotation=0)

# Gráfico 2: Distribuição das durações dos filmes
fig2, ax2 = plt.subplots(figsize=(8, 6))
df_movies = df[df['type'] == 'Movie']
ax2.hist(df_movies['duration'], bins=30, color='green', alpha=0.7)
ax2.set_xlabel('Duração (minutos)')
ax2.set_ylabel('Contagem')
ax2.set_title('Distribuição das Durações dos Filmes na Netflix')

# Exibir os gráficos no Streamlit
st.pyplot(fig1)
st.pyplot(fig2)
