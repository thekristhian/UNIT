#O usuário deverá informar a quantidade de alunos entre 2 e 7
#Informar o nome de cada aluno
#Cada aluno deverá ter duas notas que variam entre 0 e 10
#Armazena os dados
#Função para cálcular a média do aluno
#Exibir no final a média da turma, quantidade de alunos na turma, o aluno que obteve a maior média e o que obteve a menor média

def saida():
    while True:
            saida = input('Você deseja sair do sistema? Digite "s" ou "n": ')

            if not saida in 'sn' or len(saida)>1:
                print('Você não digitou uma opção válida, tente novamente')
                continue
            elif saida == 's':
                print('Até a próxima!')
                break
            else:
                break
    return saida

def verificaNome():
    flag = True
    while flag:
        nomeAluno = input('Digite o nome do aluno: ')

        if not nomeAluno.isalpha():
            print('Você não digitou um nome válido, tente novamente')
            continue
        else:
            flag = False
            return nomeAluno

def verificaNota():

    while True:
        primeiraNota = input('Digite a primeira nota do aluno: ')

        try:
            primeiraNotaValida = float(primeiraNota)
            if primeiraNotaValida > 10:
                print('Você não digitou uma nota válida')
                continue
        except ValueError:
            print('Você não digitou uma nota válida')
            continue
        
        while True:
            segundaNota = input('Digite a segunda nota do aluno: ')

            try:
                segundaNotaValida = float(segundaNota)
                if segundaNotaValida > 10:
                    print('Você não digitou uma nota válida')
                    continue
            except ValueError:
                print('Você não digitou uma nota válida')
                continue
            print('-'*40)
            break
        break

    return primeiraNotaValida, segundaNotaValida
        
def calculoMedia(nome, nota1, nota2, lista):
    media = (nota1 + nota2)/2
    lista = [nome, media]
    return lista

def exibeResultados(nomecommedia):
    
    notasTamanho = len(nomecommedia)
    notasSoma = 0
    maiorMedia = []
    menorMedia = []
    for i in range(notasTamanho):
        for j in range(len(nomecommedia[i])):
            if j == 1:
                notasSoma += nomecommedia[i][j]
                if nomecommedia[i][j] > nomecommedia[i-1][j]:
                    maiorMedia = nomecommedia[i]
                else:
                    menorMedia = nomecommedia[i]

    mediaNotas = notasSoma/notasTamanho
    
    print('-'*40)
    print(f'A média de notas da turma é: {mediaNotas}')
    print('-'*40)
    print(f'A quantidade de alunos na turma é: {notasTamanho}')
    print('-'*40)
    print(f'A maior média foi de {maiorMedia[0]} que tirou {maiorMedia[1]}')
    print('-'*40)
    print(f'menor média foi de {menorMedia[0]} que tirou {menorMedia[1]}')
    print('-'*40)


def recebeValores():
    listaTurma = []

    while True:
        quantidade = input('Digite a quantidade de alunos: ')

        try:
            quantidadeAlunos = int(quantidade)
            print('-'*40)
        except:
            print('Você não digitou uma quantidade válida')
            continue

        for i in range(quantidadeAlunos):
            listaAluno = []
            
            nomeAluno = verificaNome()

            primeiraNotaValida, segundaNotaValida = verificaNota()

            listaAluno += [nomeAluno, primeiraNotaValida, segundaNotaValida]
            listaTurma += [listaAluno]
        
        listaMedias = []
        nomeMedia = []

        for j in range(len(listaTurma)):
            for k in range(len(listaTurma[j])):
                if k == 0:
                    nomeAtual = listaTurma[j][k]
                elif k == 1:
                    notaUmAtual = listaTurma[j][k]
                elif k == 2:
                    notaDoisAtual = listaTurma[j][k]

            nomeMedia += [calculoMedia(nomeAtual, notaUmAtual, notaDoisAtual, listaMedias)]

        exibeResultados(nomeMedia)

        sair = saida()
        if sair == 's':
            break
        elif sair == 'n':
            continue
        else:
            print('Houve algum erro no programa')




def inicio():
    print('Olá! Seja bem-vindo a base de dados dos estudantes!')

    recebeValores()

inicio()