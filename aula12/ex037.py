num = int(input('Digite um número inteiro: '))
print('Escolha a base que deseja:\n   1- Binário\n   2- Octal\n   3- Hexadecimal')
option = int(input(''))

if option == 1:
    print('O número {} em binário é {}.'.format(num, bin(num)))
elif option == 2:
    print('O número {} em octal é {}.'.format(num, oct(num)))
elif option == 3:
    print('O número {} em hexadecimal é {}.'.format(num, hex(num)))
else:
    print('Favor inserir uma escolha entre as 3 opções indicadas')