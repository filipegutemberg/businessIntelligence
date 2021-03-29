#Verifique a evolução temporal de novos programas de TV/filmes nos últimos anos. Faça um gráfico de frequência ao longo do tempo, discriminando “programas de TV” e “filmes”, por ano de lançamento (release_year).
import numpy as np
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd #this is how I usually import pandas
import matplotlib #only needed to determine Matplotlib version number


path = "C:/Users/Filipe/Desktop/VISTO/MESTRADO SEMESTRE 2/BUSINESS INTELLIGENCE/Aula 03 - Sem aula Soh Exercicio/BD_Netflix.csv"
dados = pd.read_csv(path)
actores = []

print("Quais os 5 actores que mais participaram de Tv shows/filmes:")
for x in dados["cast"]:
    y = str.split(str(x), ",")
    for z in y:
        actores.append(z)


seriesActores = pd.Series(actores)
print(seriesActores.value_counts().head(n=10))

print("Quais os 5 actores que mais participaram de Tv shows/filmes:")
