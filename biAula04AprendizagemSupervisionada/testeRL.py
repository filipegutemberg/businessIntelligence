#https://stackabuse.com/linear-regression-in-python-with-scikit-learn/
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('C:/Users/Filipe/Downloads/student_scores.csv')
print(dataset.shape)
print(dataset.head())
print(dataset.describe())

dataset.plot(x='Hours', y='Scores', style='o')
plt.title('Hours vs Percentage')
plt.xlabel('Hours Studied')
plt.ylabel('Percentage Score')
# plt.show()

X = dataset.iloc[:, :-1].values #Notas
y = dataset.iloc[:, 1].values #Horas
print('IMPREIMINDO XX TRAIN')
print(X)
#Dividiu os dados para treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#Treinando o Algoritmo
regressor = LinearRegression()
regressor.fit(X_train, y_train)
print(regressor.intercept_)
print(regressor.coef_)
y_pred = regressor.predict(X_test)
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df)