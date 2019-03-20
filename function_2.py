#   Function return

import random

def getAnswer(number):
    if number == 1:
        return 'It is certain'
    elif number == 2:
        return 'It is decidedly so'
    elif number == 3:
        return 'Yes'
    elif number == 4:
        return 'Reply hazy try again'
    elif number == 5:
        return 'Ask again later'
    elif number == 6:
        return 'Concentrate and ask again'
    elif number == 7:
        return 'My reply is no'
    elif number == 8:
        return 'Outlook not so good'
    elif number == 9:
        return 'Very doubtful'

r = random.randint(1, 9) #Faz um random de (int) de 1 ate 9 e passa como parametro pra função
fortune = getAnswer(r)
print(fortune)

#pode ser compactada em apenas uma linha de código:
print(getAnswer(random.randint(1, 9)))