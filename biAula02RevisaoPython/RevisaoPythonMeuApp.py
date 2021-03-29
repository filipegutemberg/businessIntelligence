#Importar
from selenium import webdriver
import time

# delclarando método
def soma(valor1, valor2):
    return valor1 + valor2
print(soma(3,2))

#Declarando Classe
class Calculadora:
    #__init__(self) diz que sempre que instanciar a class, ele será executado primeiro, especie de construtor
    #self equivale ao this.
    def __init__(self, param1, param2):
        self.valor1 = param1
        self.valor2 = param2

    def soma(self):
        return self.valor1 + self.valor2
    def subtracao(self):
        return self.valor1 - self.valor2
CalculadoraDivisao = {
    'divisao': lambda a , b: a / b
}



def contadorDeLetras(lista_palavras):
    #lista de quantidades
    contador = []
    for x in lista_palavras:
        qtd = len(x)
        contador.append(qtd)
    return contador


    #if __name__ serva para executar o que está dentro somente se for chamado de dentro do próprio arquivo.
if __name__ == '__main__':
    print('Meu primeiro Programa!')
    # a = int(input("Digite o primeiro valor:"))
    # b = int(input("Digite o segundo valor:"))
    a = 1
    b = 2
    soma = a + b
    print(soma)
    # print('Minha soma é ' + soma) #Erro
    print('Minha soma de {} e {}  é {}'.format(a, b, soma) )
    print('Minha soma de {letraA} e {letraB}  é {sum}'.format(letraA = a, letraB = b, sum = soma) )
    print(type(soma))
    set = {a,b,1,2,'c'}
    print(set)
    meuArray = [1,2,'Filipe']
    print(meuArray)
    print(type(set))
    print(type(meuArray))


    calculadora = Calculadora(10,20)
    print("valor1: {}, valor2: {}".format(calculadora.valor1, calculadora.valor2))
    print(calculadora.subtracao())

    #chamando contador de letras
    lista = ["Ana Laura", "Filipe"]
    print(contadorDeLetras(lista))
    for x in range(5):
        print(x)

