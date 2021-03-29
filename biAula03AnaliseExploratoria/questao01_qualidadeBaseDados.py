
# Analise a qualidade e informação disponível na base de dados. Verifique que variáveis estão disponíveis, valores em falta, quais são as suas estatísticas básicas (valores médios, máximos, variância, etc…).
# Verifique qual é a proporção entre programas de TV/filmes. Faça um “pie chart” ou um gráfico de barras.

import numpy as np
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd #this is how I usually import pandas
import matplotlib #only needed to determine Matplotlib version number

path = "C:/Users/Filipe/Desktop/VISTO/MESTRADO SEMESTRE 2/BUSINESS INTELLIGENCE/Aula 03 - Sem aula Soh Exercicio/BD_Netflix.csv"
dados = pd.read_csv(path)

print("Dados que estão disponíveis para consulta:")
print(dados.columns)

print("\n---------------------------------------\n")

print("Estatísticas Básicas")

# print("Tipo:")
# print(dados["type"].describe())
# print("País")
# print(dados["country"].describe())
# print("Ano de lançamento:")
# print(dados["release_year"].describe())
# print("Avaliação:")
# print(dados["rating"].describe())
print("duração:")
print(dados["duration"].describe())

print(dados["director"].isna().describe())

print("---------------------------")
dados["type"].value_counts().plot.bar()
plt.show()
dados["type"].value_counts().plot.pie()
plt.show()
# print("Gráfico de Barras:")
# # plt.bar()
# labels = "TV Show", "Movie"
# # dados["type"].unique()
# y1 = dados[dados["type"] == "TV Show"].count()
# y2 = dados[dados["type"] == "Movie"].count()
# explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
# print(y1)
# a = [y1, y2]
# ax1 = plt.subplots()
# ax1.pie(a, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# plt.show()
# plt.plot(x,y1, color='red',linestyle='-',label='TV SHOW')
# plt.plot(x,y2, color='blue',linestyle='-',label='MOVIE')
# plt.legend(loc='upper right')
# plt.title('TV SHOW X MOVIES')
# plt.show()