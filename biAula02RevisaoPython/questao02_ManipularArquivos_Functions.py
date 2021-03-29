#W sobrescreve o conteúdo do arquivo
def escrever(fileName, text):
    arquivo = open(fileName, 'w')
    arquivo.write(text)
    arquivo.close()
#A adiciona conteúdo ao arquivo

def actualizar(fileName, text):
    arquivo = open(fileName, 'a')
    arquivo.write(text)
    arquivo.close()

def ler(fileName):
    arquivo = open(fileName, 'r')
    text = arquivo.read()
    arquivo.close()
    return text