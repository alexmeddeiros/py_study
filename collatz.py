'''
Sequência de Collatz
Crie uma função chamada collatz() que tenha um parâmetro de nome number.
Se number for par, collatz() deverá exibir number // 2 e retornar esse valor. Se
number for ímpar, collatz() deverá exibir e retornar 3 * number + 1.
Em seguida, crie um programa que permita que o usuário digite um inteiro e
fique chamando collatz() com esse número até a função retornar o valor 1.
'''


def collatz(number):
    if(number % 2) == 0:
        return number // 2
    elif(number % 2) == 1:
        return(3 * number) + 1


print('Digite um numero para a função Collatz:')
i = int(input())
while i > 1:
    i = collatz(i)
    print(i)
