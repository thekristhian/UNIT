#O usuário deverá informar a base e a altura de um triângulo
#Deverá criar uma função para calcular a área de um triângulo
#Exibir o valor da base, o da altura e da área

def saida():
    while True:
            saida = input('Você deseja sair? Digite s ou n: ')

            if not saida in 'sn' or len(saida)>1:
                print('Você não digitou uma opção válida, tente novamente')
                continue
            elif saida == 's':
                print('Até a próxima!')
                break
            else:
                break
    return saida

def calculaArea(base, altura):
    areaTriangulo = (base * altura) / 2
    print(f'A área do triângulo de base {base} e altura {altura} é: {areaTriangulo}')

def recebeValor():
    while True:
        base = input('Insira o valor da base do triângulo: ')
        try:
            baseNumber = float(base)
        except:
            print('Você não digitou um valor válido, tente novamente')
            continue
        
        altura = input('Insira o valor da altura do triângulo: ')
        try:
            alturaNumber = float(altura)
        except:
            print('Você não digitou um valor válido, tente novamente')
            continue
        calculaArea(baseNumber, alturaNumber)
        
        sair = saida()
        if sair == 's':
            break
        elif sair == 'n':
            continue
        else:
            print('Houve algum erro no programa')




def inicio():
    print('Olá, seja bem-vindo!')
    recebeValor()

inicio()