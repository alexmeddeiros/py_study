def somar():
    try:
        x = int(input('Digite o primeiro valor:\n'))
        y = int(input('Digite o segundo valor:\n'))
        print('O resultado é %s' %(x + y))
    except:
        print('Valor inválido')


def subtrair():
    try:
        x = int(input('Digite o primeiro valor:\n'))
        y = int(input('Digite o segundo valor:\n'))
        print('O resultado é %s' %(x - y))
    except:
        print('Valor inválido')


def multiplicar():
    try:
        x = int(input('Digite o primeiro valor:\n'))
        y = int(input('Digite o segundo valor:\n'))
        print('O resultado é %s' %(x * y))
    except:
        print('Valor inválido')



def dividir():
    try:
        x = int(input('Digite o primeiro valor:\n'))
        y = int(input('Digite o segundo valor:\n'))
        print('O resultado é %s' %(x / y))
    except:
        print('Valor inválido')


def menu():
    print('Digite uma opção pra continuar:\n')
    print('1 - Somar')
    print('2 - Subtrair')
    print('3 - Multiplicar')
    print('4 - Dividir\n')


def iniciar():
    menu()
    try:
        opcao_selecionada = int(input())

        if opcao_selecionada == 1:
            somar()
        elif opcao_selecionada == 2:
            subtrair()
        elif opcao_selecionada == 3:
            multiplicar()
        elif opcao_selecionada == 4:
            dividir()
        else:
            print('Valor inválido!')
    except:
        print('valor inválido')


iniciar()