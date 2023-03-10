n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
if n1 == n2:
    print('\033[1;34mOs dois números são iguais!\033[m')
elif n1 > n2:
    print('O número \033[1;31m{}\033[m é maior!'.format(n1))
else:
    print('O número \033[1;33m{}\033[m é maior!'.format(n2))
