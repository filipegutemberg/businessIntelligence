

#Identifique quem são os principais realizadores, nas diversas categorais. Faça um gráfico de frequências com os 8 principais realizadores, para programas de TV e filmes.

import numpy as np
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd #this is how I usually import pandas
import matplotlib #only needed to determine Matplotlib version number

path = "C:/Users/Filipe/Desktop/VISTO/MESTRADO SEMESTRE 2/BUSINESS INTELLIGENCE/Aula 03 - Sem aula Soh Exercicio/BD_Netflix.csv"
dados = pd.read_csv(path)

def principaisRealizadores():
    x = dados["director"].value_counts().head(n=8)
    x.plot.bar()
    print(x)


if __name__ == '__main__':
    print("Dados que estão disponíveis para consulta:")
    print(dados.columns)
    principaisRealizadores()

    plt.show()




