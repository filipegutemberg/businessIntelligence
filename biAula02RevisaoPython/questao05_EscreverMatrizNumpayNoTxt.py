import numpy as npy
import questao02_ManipularArquivos_Functions

#ENUNCIADO
#Crie uma matriz, de 10 linhas e 5 colunas, com números inteiros aleatórios entre 0 e 1000.
# Guarde essa matriz num ficheiro de dados, com as colunas separadas por TAB.
# Guarde a mesma matriz num ficheiro de dados, com as colunas separadas por vírgulas.


def matrixToText(ficheiro, separador):
    for x in a:
        for y in x:
            questao02_ManipularArquivos_Functions.actualizar(ficheiro, str(y))
            questao02_ManipularArquivos_Functions.actualizar(ficheiro, separador)
        questao02_ManipularArquivos_Functions.actualizar(ficheiro, "\n")

path = 'C:/Users/Filipe/Desktop/VISTO/MESTRADO SEMESTRE 2/BUSINESS INTELLIGENCE/Aula 02 - Revisao de Python/meuArquivo.txt'
path2 = 'C:/Users/Filipe/Desktop/VISTO/MESTRADO SEMESTRE 2/BUSINESS INTELLIGENCE/Aula 02 - Revisao de Python/meuArquivo2.txt'
#reiniciar arquivo de dados
questao02_ManipularArquivos_Functions.escrever(path, "")
questao02_ManipularArquivos_Functions.escrever(path2, "")
a = npy.floor(1000*npy.random.random(50)).reshape((10, 5)) #arrayNumpay a ser persistido pela função.
print(a)
matrixToText(path, "	")
matrixToText(path2, ";")



# for x in a:
#     for y in x:
#         questao02_Parte01.actualizar(path,str(y))
#         questao02_Parte01.actualizar(path,"	")
#    questao02_Parte01.actualizar(path,"\n")