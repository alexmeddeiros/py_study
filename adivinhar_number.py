#Este é um jogo de adivinhaçao

import random
secretNumber = random.randint(1, 20)
print('Eu acho que e um numero entre 1 e 20')

#peça para o jogador adivinhar o numero em até 6 tentativas
for guessesTaken in range(1,7):
    print('Dẽ um palpite:\n')
    guess = int(input())

    if guess < secretNumber:
        print('Seu palpite é baixo')
    elif guess > secretNumber:
        print('Seu palpite é auto')
    else:
        break #essa condicao corresponde ao palpite correto


if guess == secretNumber:
    print('Muito bom!" você advinhou o numero em ' +str(guessesTaken)+' tentativas!')
else:
    print('Nao acertou. o numero que eu estava pensando era: '+str(secretNumber))
