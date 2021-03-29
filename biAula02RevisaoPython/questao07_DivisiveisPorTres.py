
#Enunciado
#Implemente um programa para determinar os números divisores por 3 de um array numpy com 20 elementos criado aleatoriamente num determinado intervalo [0,70].
import numpy as npy

a = npy.int_(70*npy.random.random(20))
print(a)
for x in a:
    if x % 3 == 0:
        print(x)