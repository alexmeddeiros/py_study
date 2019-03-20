'''
Quando um código em uma cláusula try provocar um erro, a execução do
programa será transferida imediatamente para o código na cláusula except.
'''

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("Error: Argumento inválido")


print(spam(2))
print(spam(0)) #Um ZeroDivisionError ocorre sempre que você tenta dividir um número por zero.
print(spam(1))
print(spam(12))