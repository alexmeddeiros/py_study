'''
O Usuário armazena o numero de sua escolha em uma das duas lista, podendo repetir o
processo quantas vezes quiser e no final ele escolhe qual exibir
'''


print("LISTA DE ARMAZENAMENTO \n Digite o numero a armazenar:")
number = input()
lista1 = []
lista2 = []



print("Escolha a lista pra armazenar:")
list = input()

if (list == '1'):
   lista1.append(number)
elif (list == '2'):
   lista2.append(number)
else:
   print('Lista informada nao existe')


print("Adicionar mais numeros?\n1 = SIM\n2 = NAO")
res = input()

while(res == '1'):
    print("Digite o numero a armazenar:")
    number = input()

    print("Escolha a lista pra armazenar:")
    list = input()

    if (list == '1'):
        lista1.append(number)
        print('Salvo na lista1')
    elif (list == '2'):
        lista2.append(number)
        print('Salvo na lista2')
    else:
        print('Lista informada nao existe')

    print("Adicionar mais numeros?\n1 = SIM\n2 = NAO")
    res = input()



print('Qual lista você quer exibir: 1 ou 2?')
choice = input()
if(choice == '1'):
    print(lista1)
elif(choice == '2'):
    print(lista2)
else:
    print('lista nao encontrada')
