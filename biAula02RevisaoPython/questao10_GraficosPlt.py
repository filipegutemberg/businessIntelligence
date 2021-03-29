
# ENUNCIADO
#
# Utilizando os dados de precipitação total anual (mm) do ficheiro PrecipitacaoPT.csv, faça alguns gráficos básicos, de linhas (função plot) e de pontos (função scatter). Represente, por exemplo:
# a) A evolução temporal da precipitação em Viana do Castelo (Figura 1 – série temporal)
# b) A precipitação total em Viana do Castelo versus Porto (Figura 2 –diagrama de dispersão).
# Personalize as figuras (título, eixos, legendas, etc).
# Grave as figuras em diversos formatos, adequados para inserir num relatório.


from pandas import DataFrame, read_csv
import pandas as pd #this is how I usually import panda
import matplotlib.pyplot as plt
import numpy as npy

path = "C:/Users/Filipe/Desktop/VISTO/MESTRADO SEMESTRE 2/BUSINESS INTELLIGENCE/Aula 02 - Revisao de Python/PrecipitacaoPT.csv"
dados = pd.read_csv(path)

# print(dados)
# x = dados["Ano"]
# y1 = dados["Viana do Castelo"]
# plt.plot(x,y1,color='red',linestyle='-',label='Viana do Castelo')
# plt.legend(loc='upper right')
# plt.show()

x = dados["Ano"]
y1 = dados["Viana do Castelo"]
y2 = dados["Porto"]
plt.plot(x,y1,color='red',linestyle='-',label='Viana do Castelo')
plt.plot(x,y2,color='blue',linestyle='-',label='Porto')
plt.legend(loc='upper right')
plt.title('Precipitação Anual')
plt.savefig('fig1.png')
plt.savefig('fig1.jpg')
plt.show()
