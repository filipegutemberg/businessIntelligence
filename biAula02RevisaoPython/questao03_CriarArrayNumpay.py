import random
from numpy.random import randn

dados = { i : random.random () for i in range (10) }
print (dados)


dados2 = { i : randn () for i in range (10) }
print (dados2)