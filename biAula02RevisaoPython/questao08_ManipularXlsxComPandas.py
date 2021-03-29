#ENUNCIADO
#
#A representação e manipulação de estruturas de dados é a principal componente da biblioteca pandas. Implemente um programa que permita importar os dados de precipitação total anual (mm) do ficheiro PrecipitacaoPT.csv.
#De seguida calcule algumas estatísticas básicas para cada cidade (valores mínimo, máximo, médio,etc.).
#NOTA: É também facultado o ficheiro PrecipitaçãoPT.xlsx, para que possa consultar a metainformação.




#Referencias: https://pandas.pydata.org/pandas-docs/version/0.15/tutorials.html
#https://medium.com/data-hackers/uma-introdu%C3%A7%C3%A3o-simples-ao-pandas-1e15eea37fa1

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

# Enable inline plotting
# %matplotlib inline
def naoExcutar():
    print('Python version ' + sys.version)
    print('Pandas version ' + pd.__version__)
    print('Matplotlib version ' + matplotlib.__version__)

    #Uma Series é como um array unidimensional
    #Abaixo criamos uma Series notas, o index desta Series é a coluna à esquerda, que vai de 0 a 4 neste caso, que o pandas criou automaticamente, já que não especificamos uma lista de rótulos.
    notas = pd.Series([2,7,5,10,6])
    print(notas)

    #verificar os atributos da nossa Series, comecemos pelos valores e o índice, os dois atributos fundamentais nesta estrutura:
    print("Valores da Serie Notas: ")
    print(notas.values)
    print("Índices da Serie Notas:")
    print(notas.index)


##Leitura de Dados CSV
path = "C:/Users/Filipe/Desktop/VISTO/MESTRADO SEMESTRE 2/BUSINESS INTELLIGENCE/Aula 02 - Revisao de Python/PrecipitacaoPT.csv"
dados = pd.read_csv(path)
# print(dados)


#Por padrão .head() exibe as 5 primeiras linhas, mas isso pode ser alterado: dados.head(n=10)
# print(dados.head())
print(type(dados))
print("Precipitacao Máx de Bejas: {}".format(dados["Beja"].max()))
print("Precipitacao Mín de Bejas: {}".format(dados["Beja"].min()))
print("Precipitacao Média de Bejas: {}".format(dados["Beja"].mean()))
# As outras colunas estão a dar erro, por conta dos espaços nos números

#Importando a grelha Metainformação do xlsx
path2 = "C:/Users/Filipe/Desktop/VISTO/MESTRADO SEMESTRE 2/BUSINESS INTELLIGENCE/Aula 02 - Revisao de Python/PrecipitacaoPT.xlsx"
dados2 = pd.read_excel(path2, sheet_name="Metainformação")
print(dados2)

