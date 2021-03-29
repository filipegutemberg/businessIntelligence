#
#ENUNCIADO
#
#Implemente um programa que utilize um array numpy para determinar os números primos num determinado intervalo de valores inteiros, por exemplo o intervalo [0,90].
import numpy as npy

primos = npy.array([])

i = 0
find = True
for x in range(0,1000):
    y = 2
    while y <= x:
        if y == x:
            primos = npy.append(primos, x)
            # print(primos)
        elif x % y == 0:
            break
        y += 1
print(primos)