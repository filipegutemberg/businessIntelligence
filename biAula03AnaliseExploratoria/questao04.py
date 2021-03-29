
# • Qual foi a evolução dos programas de TV disponíveis na Netflix na última década? E dos filmes?
# • Quais são as principais categorias de programas de TV/filmes?
# • Qual é a duração média dos programas de TV/filmes? Em que categorias?
# • Quem são os principais realizadores dos programas de TV/filmes?
# • Quais são os países com maior número de programas de TV/filmes?
# • Que tipo de conteúdos estão disponíveis dos diferentes países?

#Implemente um programa que permita responder às restantes questões acima.
import numpy as np
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd #this is how I usually import pandas
import matplotlib #only needed to determine Matplotlib version number
import questao02_evolucaoTemporalGrafico as evolutions
import questao03_listarPricipaisRealizadores as realizadores

path = "C:/Users/Filipe/Desktop/VISTO/MESTRADO SEMESTRE 2/BUSINESS INTELLIGENCE/Aula 03 - Sem aula Soh Exercicio/BD_Netflix.csv"
dados = pd.read_csv(path)


print("Qual foi a evolução dos programas de TV disponíveis na Netflix na última década? E dos filmes?")
# evolutions.tvShowEvolution()
# evolutions.MovieEvolution()

print("Quais são as principais categorias de programas de TV/filmes?")
def top10Categorias():
    topCategorias = []
    for x in dados['listed_in'].array:
        y = str.split(x,",")
        for z in y:
            topCategorias.append(z)

    seriesTopCategorias = pd.Series(topCategorias)
    print(seriesTopCategorias.value_counts().head(n=10))
# top10Categorias()

print("Qual é a duração média dos programas de TV/filmes? Em que categorias?")
duracoesMin = []
duracoesSeason = []
def duracaoMedia():
    for x in dados["duration"]:
        if("min" in x):
            duracoesMin.append(int(x[:-4]))
        else:
            duracoesSeason.append(int(x[:-7]))
    seriesDuracoesMin = pd.Series(duracoesMin)
    seriesDuracoesSeason = pd.Series(duracoesSeason)
    print("Duração Média Dos Filmes em Minutos {}".format(seriesDuracoesMin.mean()))
    print("Duração Média Dos Filmes em Temporadas {}".format(seriesDuracoesSeason.mean()))

# duracaoMedia()

print("Quem são os principais realizadores dos programas de TV/filmes?")
print(realizadores.principaisRealizadores())

print("Quais são os países com maior número de programas de TV/filmes?")
print(dados["country"].value_counts().head(n=8))

print("Que tipo de conteúdos estão disponíveis dos diferentes países?")

# choice = input("Infome o País para o qual deseja saber o conteúdo:")
categoriasPais = []
for x in dados[dados["country"] == "Argentina"]["listed_in"]:
    y = str.split(x, ",")
    for z in y:
        categoriasPais.append(z)
print("Conteúdo de Argentina.")
seriesCategoriasPais = pd.Series(categoriasPais)
print(seriesCategoriasPais.unique())


# print(dados[dados["country"] == "Argentina"]["listed_in"].unique())
