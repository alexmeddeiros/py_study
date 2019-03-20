#   Argumentos nomeados e print()

print('Hello')
print('World')
print('\n')

print('Hello ', end='') #argumentos nomeados
print('World')
print('\n')

'''
De modo semelhante, ao passar diversos valores de string a print(), a função
as separará automaticamente com um único espaço. Digite o seguinte no shell
interativo:
'''
print('cats', 'dogs', 'mice')




'''
Porém você pode substituir a string default de separação passando o
argumento nomeado sep. Digite o seguinte no shell interativo:
'''
print('cats', 'dogs', 'mice', sep=',')