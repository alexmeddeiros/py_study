def hello():
    print("This is a funtion")
    print('function is cool!')
    print("it's possible to do many things\n")

hello()


#Instruções def com parâmetros

def hello(name):
    print("hi, "+str(name))

hello(input()) #recebe o nome pelo prompt