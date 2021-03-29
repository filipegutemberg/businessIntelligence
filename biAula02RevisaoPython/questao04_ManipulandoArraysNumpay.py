#Referências: https://medium.com/ensina-ai/entendendo-a-biblioteca-numpy-4858fde63355

import numpy as npy
import questao02_ManipularArquivos_Functions

path = 'C:/Users/Filipe/Desktop/VISTO/MESTRADO SEMESTRE 2/BUSINESS INTELLIGENCE/Aula 02 - Revisao de Python/meuArquivo.txt'

#criando array numpy simples
v = npy.array ([4,6,3,32,99,47,100,25])
print("Array v:")
print (v)
#O atributo shape retorna uma tupla que consiste nas dimensões da Array, mostrando quantas linha e colunas temos para exemplificar.
print("Shape de Array v:")
print (v.shape)

#ndim Return the number of dimensions of an array.
print("ndim (#dimensoes de array v)")
print(v.ndim)
print("Tamanho array v:")
print(len(v))
M = npy.array ( [ [5,16,23,12],[49,7,100,15] ] )
print("Array M: {}".format(M))
print("ndim (#dimensoes de array M)")
print(M.ndim)
print("Tamanho array M:")
print(len(M))
print(M.shape)

#Cria um array 3 linhas e duas colunas
a = npy.arange(6).reshape((3, 2))
print("Cria um array 3 linhas e duas colunas:")
print(a)
#Array NumPy vazia? podemos usar a função empty, Ele cria uma Array não inicializada e dtype especificados: np.empty(shape, dtype = float, order = 'C')
#O código a seguir mostra um exemplo de uma Array NumPy vazia:
#Os elementos abaixo mostram valores aleatórios, pois não são inicializados.
print("O código a seguir mostra um exemplo de uma Array NumPy vazia:")
x = npy.empty([3,2], dtype = int)
print(x)
#criar um Array NumPy que retorne todos os valores 0
my_new_array = npy.zeros((5))
print(my_new_array)
#nós também temos a função ones e de forma semelhante retornaremos:
my_new_array_ones = npy.ones((5))
print(my_new_array_ones)

#E se quisermos criar uma Array de valores aleatórios?
my_random_array = npy.random.random((5))
print(my_random_array)

#Vamos imprimir números aleatorios que esteja entre 0 e 10:
print("Vamos imprimir números aleatorios que esteja entre 0 e 10:")
a = npy.floor(10*npy.random.random((3,4)))
print(a)

# 3x3 matrix with 1's on main diagonal
obj1 = npy.eye(3, dtype = float)
print("Matrix : \n", obj1)
# matrix with Row=2 Column=3 and diagonal=1
obj2 = npy.eye(2, 3, k = 1)
print("\nMatrix : \n", obj2)

x = npy.arange(9).reshape((3,3))
print("Matriz X: \n{}".format(x))
diagonalPrincipalX = npy.diag(x)
print("Diagonal da matriz X é {}".format(diagonalPrincipalX))
diagonalAcimaX = npy.diag(x, k=1)
print("Diagonal Acima da matriz X é {}".format(diagonalAcimaX))
diagonalAbaixoX = npy.diag(x, k=-1)
print("Diagonal Abaixo da matriz X é {}".format(diagonalAbaixoX))


questao02_ManipularArquivos_Functions.escrever(path, str(obj1))