import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/content/netflix_titles.csv', encoding='latin-1')


title_types = df['type'].value_counts()
title_types.plot(kind='bar', color=['blue', 'pink'])
plt.xlabel('Tipo de Título')
plt.ylabel('Contagem')
plt.title('Contagem de Títulos na Netflix por Tipo')
plt.xticks(rotation=0)  
plt.show()
