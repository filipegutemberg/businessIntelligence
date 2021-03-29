#Verifique a evolução temporal de novos programas de TV/filmes nos últimos anos. Faça um gráfico de frequência ao longo do tempo, discriminando “programas de TV” e “filmes”, por ano de lançamento (release_year).


import numpy as np
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd #this is how I usually import pandas
import matplotlib #only needed to determine Matplotlib version number

path = "C:/Users/Filipe/Desktop/VISTO/MESTRADO SEMESTRE 2/BUSINESS INTELLIGENCE/Aula 03 - Sem aula Soh Exercicio/BD_Netflix.csv"
dados = pd.read_csv(path)

def tvShowEvolution():
    x = dados[dados["type"] == "TV Show"].groupby("release_year")["type"].count()
    x.plot.bar()
    plt.show()

def MovieEvolution():
    x = dados[dados["type"] == "Movie"].groupby("release_year")["type"].count()
    plt.title('Movie')
    x.plot.bar()
    plt.show()

if __name__ == '__main__':
    tvShowEvolution()
    MovieEvolution()

#dados[dados["type"] == "TV Show"].groupby("release_year")["type"].count().plot().bar
# y2 = dados[dados["type"] == "Movie"].groupby("release_year")["type"].count()


# plt.plot(x,y1,color='red',linestyle='-',label='TV Show')
# plt.plot(x,y2,color='blue',linestyle='-',label='Movie')
# plt.legend(loc='upper right')
# plt.title('Lançamentos por Ano')

# plt.show()
# print(x)
# print(y1)
# print(y2)