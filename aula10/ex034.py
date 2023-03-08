sal = float(input('Insira o valor do salário: R$'))
if sal > 1250.00:
    print('O seu salário terá aumento de 10%, totalizando R${:.2f}'.format(sal*1.1))
else:
    print('O seu salário terá aumento de 15%, totalizando R${:.2f}.'.format(sal*1.15))
