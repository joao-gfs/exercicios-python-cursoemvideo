num = int(input('Digite um número inteiro: '))
print('Escolha a base que deseja:\n   [1] Binário\n   [2] Octal\n   [3] Hexadecimal')
option = int(input('    '))

if option == 1:
    print('O número {} em binário é {:b}.'.format(num, num))
elif option == 2:
    print('O número {} em octal é {:o}.'.format(num, num))
elif option == 3:
    print('O número {} em hexadecimal é {:x}.'.format(num, num))
else:
    print('Opção inválida! Tente novamente!')
