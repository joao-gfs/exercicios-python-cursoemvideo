from random import randint
from time import sleep
n = randint(0, 5)
tentativa = int(input('\033[7;97mAdivinhe o número secreto entre 0 e 5:\033[m '))
print('\033[1;33m-=-\033[m'*25)
print('\033[4;35mPROCESSANDO...\033[m')
sleep(2)
if tentativa == n:
    print('\033[1;32mVocê acertou!!! O número secreto é {}!!!\033[m'.format(n))
else:
    print('\033[1;31mVocê errou o número secreto! O computador tinha pensado no {}!\033[m'.format(n))
