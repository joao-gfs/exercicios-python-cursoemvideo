nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
med = (nota1 + nota2)/2
if med < 5:
    print('Sua média é de {:.1f} e está abaixo de \033[1;31m5.0\033[m, portanto você está \033[1;31mREPROVADO\033[m!'.format(med))
elif 5 <= med < 7:
    print('Sua média é de {:.1f} e está acima de \033[1;31m5.0\033[m mas abaixo de \033[1;32m7.0\033[m, portanto você está em \033[1;33mRECUPERAÇÃO\033[m!'.format(med))
else:
    print('Sua média é de {:.1f} e está acima de \033[1;32m7.0\033[m, portanto você está \033[1;32mAPROVADO\033[m!'.format(med))
