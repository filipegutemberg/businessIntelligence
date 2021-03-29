#Referencias: https://pandas.pydata.org/pandas-docs/version/0.15/tutorials.html
#https://medium.com/data-hackers/uma-introdu%C3%A7%C3%A3o-simples-ao-pandas-1e15eea37fa1
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html

#Gráfico de dispersão referências:
#https://pythonspot.com/matplotlib-scatterplot/

# Import all libraries needed for the tutorial

# General syntax to import specific functions in a library:
##from (library) import (specific library function)
from pandas import DataFrame, read_csv

# General syntax to import a library but no functions:
##import (library) as (give the library a nickname/alias)
import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import seaborn as sb

path = "C:/Users/Filipe/Desktop/VISTO/MESTRADO SEMESTRE 2/BUSINESS INTELLIGENCE/Aula 02 - Revisao de Python/PrecipitacaoPT.csv"
dados = pd.read_csv(path)
print("Dados Disponíveis:")
print(dados.columns)

print("Faça a análise exploratória dos dados e selecione séries de precipitação total (mm) de duas cidades.")
# print(dados["Viana do Castelo"])
# print(dados["Porto"])

print("Gráfico de dispersão:")
# dados.plot.scatter(x='Ano', y='Viana do Castelo')
# plt.title("Precipitação Anual Viana do Castelo")
print('Utilize a biblioteca pandas para ler e filtrar o conjunto de dados.')
print(dados[dados['Ano']>2010])

print('Utilize a biblioteca matplotlib para preparar e apresentar o diagrama de dispersão.')

#colors = ("red", "green")
#groups = ("Viana do Castelo", "Porto")
# Create plot
matplotlib.pyplot.scatter(dados['Porto'], dados['Viana do Castelo'], s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, edgecolors=None, plotnonfinite=False, data=None, label='')
# matplotlib.pyplot.scatter(dados['Ano'], dados['Porto'], s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, edgecolors=None, plotnonfinite=False, data=None, label='Porto')
plt.xlabel('Porto (mm)')
plt.ylabel('Viana do Castelo (mm)')
plt.title("Precipitação Viana do Castelo vs Porto (mm)")
plt.show()

print('Utilize a biblioteca numpy para efetuar o arredondamento da previsão.')
#https://medium.com/@diegosantosseabra/scikit-learn-python-linear-regression-predicting-the-sex-of-a-person-df72700a0732
#Este resolveu o caso:
#https://stackabuse.com/linear-regression-in-python-with-scikit-learn/
print('a) Construa o modelo de regressão linear e treine-o, utilizando os primeiros 25 anos da série;')
# regression = LinearRegression()
# X = dados[['Viana do Castelo', 'Ano']]
# X = X[X['Ano']<=1995]
# Y = dados[dados['Ano'] <= 1995]['Porto']
# print('b) Teste o modelo utilizando os restantes 25 anos da série;')
# X_train, X_test, y_train, y_test = train_test_split(X, Y)
# print(X_train)
# print(y_train)
# regression.fit(X_train, y_train)
# predictions = regression.predict(X_test)
# print(predictions)
print('c) Faça a representação gráfica (diagrama de dispersão, recta de regressão, R²);')
# sb.distplot(y_test - predictions, axlabel="Test - Prediction")
# plt.show()
print('d) Utilize o modelo para prever a precipitação na cidade 2, conhecendo o valor de precipitação na cidade 1.')
print('e) Escreva a equação do modelo. Indique o coeficiente de determinação (R²) e comente.')
