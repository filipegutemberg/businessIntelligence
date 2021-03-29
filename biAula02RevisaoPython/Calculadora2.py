class Calculadora:
    #__init__(self) diz que sempre que instanciar a class, ele será executado primeiro, especie de construtor
    #self equivale ao this.
    #Nesse caso o __init__(self) é desnecessário e poderia ser removido.
    def __init__(self):
        pass

    def soma(self, valor1, valor2):
        return valor1 + valor2
    def subtracao(self, valor1, valor2):
        return valor1 - valor2

calculadora = Calculadora()
print(calculadora.subtracao(3,2))