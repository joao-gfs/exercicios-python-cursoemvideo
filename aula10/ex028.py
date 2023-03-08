from random import randint
from time import sleep
n = randint(0, 5)
tentativa = int(input('Adivinhe o número secreto entre 0 e 5: '))
print('-=-'*25)
print('PROCESSANDO...')
sleep(2)
if tentativa == n:
    print('Você acertou!!! O número secreto é {}!!!'.format(n))
else:
    print('Você errou o número secreto! O computador tinha pensado no {}!'.format(n))
