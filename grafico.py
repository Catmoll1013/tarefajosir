import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('netflix_titles.csv', encoding='latin-1')


title_types = df['type'].value_counts()
title_types.plot(kind='bar', color=['blue', 'pink'])
plt.xlabel('Tipo de Título')
plt.ylabel('Contagem')
plt.title('Contagem de Títulos na Netflix por Tipo')
plt.xticks(rotation=0)
plt.figure(figsize=(10, 6))  

plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st  # Importe a biblioteca Streamlit

df = pd.read_csv('netflix_titles.csv', encoding='latin-1')

# Exibe uma mensagem antes de plotar o gráfico
st.write("Antes de plotar o gráfico")

title_types = df['type'].value_counts()
title_types.plot(kind='bar', color=['blue', 'pink'])
plt.xlabel('Tipo de Título')
plt.ylabel('Contagem')
plt.title('Contagem de Títulos na Netflix por Tipo')
plt.xticks(rotation=0)  
plt.show()

# Exibe uma mensagem após plotar o gráfico
st.write("Depois de plotar o gráfico")
