from emoji import emojize
from random import choice
from time import sleep

jokenpo = ['pedra', 'papel', 'tesoura']
computer = choice(jokenpo)
emop = ''
emoc = ''
winner = ''

print(emojize(':raised_hand_with_fingers_splayed: :v: :punch: \033[1;31mJo\033[1;33mKen\033[1;32mPô\033[m :punch: :v: :raised_hand_with_fingers_splayed:', language='alias'))
print('Bem vindo ao \033[1mJoKenPô\033[m. Escolha entre \033[1mPedra\033[m, \033[1mPapel\033[m ou \033[1mTesoura\033[m e tente vencer o computador')
player = input('Digite sua tentativa: ').lower().strip()

if player != 'pedra' and player != 'papel' and player != 'tesoura':
    print('\033[4;31mIsso não é uma opção válida. Tente novamente!\033[m')
else:

    print('\033[1;31mJo\033[m')
    sleep(0.5)
    print('\033[1;33mKen\033[m')
    sleep(0.5)
    print('\033[1;32mPô\033[m')
    sleep(0.5)

    if player == 'pedra':
        emop = ':punch:'
    elif player == 'papel':
        emop = ':raised_hand_with_fingers_splayed:'
    elif player == 'tesoura':
        emop = ':v:'
    else:
        print('\033[4;31mIsso não é uma opção válida\033[m')

    if computer == 'pedra':
        emoc = ':punch:'
    elif computer == 'papel':
        emoc = ':raised_hand_with_fingers_splayed:'
    elif computer == 'tesoura':
        emoc = ':v:'

    print(emojize('Jogador: {}'.format(emop), language='alias'))
    print(emojize('Computador: {}'.format(emoc), language='alias'))
    sleep(0.5)

    if player == 'pedra':
        if computer == 'pedra':
            print('\033[1;33mEmpate!\033[m')
        elif computer == 'papel':
            print('\033[1;31mO Computador venceu :/\033[m')
        elif computer == 'tesoura':
            print('\033[1;32mVocê venceu!!!\033[m')
    elif player == 'papel':
        if computer == 'papel':
            print('\033[1;33mEmpate!\033[m')
        elif computer == 'tesoura':
            print('\033[1;31mO Computador venceu :/\033[m')
        elif computer == 'pedra':
            print('\033[1;32mVocê venceu!!!\033[m')
    elif player == 'tesoura':
        if computer == 'tesoura':
            print('\033[1;33mEmpate!\033[m')
        elif computer == 'pedra':
            print('\033[1;31mO Computador venceu :/\033[m')
        elif computer == 'papel':
            print('\033[1;32mVocê venceu!!!\033[m')
