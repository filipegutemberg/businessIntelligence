import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#Baseado em:
#https://stackabuse.com/linear-regression-in-python-with-scikit-learn/
#https://stackoverflow.com/questions/40941542/using-scikit-learn-linearregression-to-plot-a-linear-fit

#Importando os dados
path = "C:/Users/Filipe/Desktop/VISTO/MESTRADO SEMESTRE 2/BUSINESS INTELLIGENCE/Aula 02 - Revisao de Python/PrecipitacaoPT.csv"
dataset = pd.read_csv(path)
print(dataset.shape)
print(dataset.head())
print(dataset.describe())

#Visualizando os dados
# dataset.plot(x='Viana do Castelo', y='Porto', style='o')
# plt.title('Viana do Castelo vs Porto')
# plt.xlabel('Viana do Castelo')
# plt.ylabel('Porto')
# plt.show()

#Separando base
X = dataset.iloc[:, 1:2].values #Viana do Castelo
y = dataset.iloc[:, 3].values #Porto


#Dividir os dados para treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)

#Treinando o Algoritmo com os 25 anos restantes
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#Imprimindo dataframe com predições
print(regressor.intercept_)
#O coeficiente abaixo indica que uma alteração no de 1 mm em Porto aumentará em 0.49% a precipitação de Viana do Castelo
print(regressor.coef_)
y_pred = regressor.predict(X_test)
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df)

plt.scatter(X, y,color='b')
plt.plot(X, regressor.predict(X),color='g')
plt.title('Viana do Castelo vs Porto')
plt.xlabel('Viana do Castelo (mm)')
plt.ylabel('Porto (mm)')
plt.savefig('fig1.png')
plt.show()
