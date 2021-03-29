
#enunciado
# A visualização gráfica dos dados é efetuada através do módulo matplotlib, que permite a utilização de funções de visualização de dados em duas dimensões (2D). Comece por fazer e personalizar figuras simples como seja a representação das funções trigonométricas seno e cosseno (exemplo de gráfico simples de linhas, plot).

import numpy as npy
import matplotlib.pyplot as plt
x = npy.linspace(-npy.pi*2, npy.pi*2,256)

y1=npy.sin(x)
y2=npy.cos(x)
plt.plot(x,y1,color='red',linestyle='-',label='seno')
plt.plot(x,y2,color='blue',linestyle=':',label='cosseno')
plt.legend(loc='upper right')
plt.show()