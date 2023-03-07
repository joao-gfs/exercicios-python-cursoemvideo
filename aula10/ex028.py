from random import randint
n = randint(0, 5)
tentativa = int(input('Adivinhe o número secreto entre 0 e 5: '))
if tentativa == n:
    print('Você acertou!!! O número secreto é {}!!!'.format(n))
else:
    print('Você errou o número secreto! O computador venceu!')
