import questao02_ManipularArquivos_Functions
# Press the green button in the gutter to run the script.

def calculaMedia(lista_alunos):
    media = 0
    media = lambda notas : sum([int(i) for i in lista_alunos])/4
    print(media(lista_alunos))

if __name__ == '__main__':
    path = 'C:/Users/Filipe/Desktop/VISTO/MESTRADO SEMESTRE 2/BUSINESS INTELLIGENCE/Aula 02 - Revisao de Python/meuArquivo.txt'
    path2 = 'C:/Users/Filipe/Desktop/meuArquivo.txt'

    #Escrevendo em diretórios diferentes
    questao02_ManipularArquivos_Functions.escrever(path, "escrevendo")
    print(questao02_ManipularArquivos_Functions.ler(path))
    questao02_ManipularArquivos_Functions.escrever(path2, "brincando")
    questao02_ManipularArquivos_Functions.ler(path2)

    #Escrevendo, lendo e botando em variáveis
    aluno1 = 'Matheus,15,10,9\n'
    aluno2 = 'Filipe,11,13,10\n'
    aluno3 = 'Rodrgio,12,12,13'
    questao02_ManipularArquivos_Functions.escrever(path, aluno1)
    questao02_ManipularArquivos_Functions.actualizar(path, aluno2)
    questao02_ManipularArquivos_Functions.actualizar(path, aluno3)
    alunos = questao02_ManipularArquivos_Functions.ler(path).split('\n')
    for x in alunos:
        tupla = x.split(",")
        print(tupla.pop(0))
        # print(tupla)
        print(calculaMedia(tupla))





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
