price = float(input('Insira valor da casa desejada: R$'))
wage = float(input('Insira o valor do seu salário mensal: R$'))
years = int(input('Insira a quantidade de anos em que deseja pagar: '))
monthp = price / (years * 12)
ppercent = monthp / wage
if ppercent > 0.3:
    print('Empréstimo \033[1:31mNEGADO!\033[m\nO valor das parcelas seria de \033[1:31mR${:.2f}\033[m'.format(monthp))
    print('Escolha outro período de pagamento ou um imóvel mais barato, pois as opções atuais comprometem \033[1:31m{:.2f}%\033[m do seu salário'.format(ppercent*100))
else:
    print('Empréstimo \033[1:32mAPROVADO!\033[m\nO valor das parcelas será de \033[1:32mR${:.2f}\033[m, representando \033[1:32m{:.2f}%\033[m do seu salário.'.format(monthp, ppercent*100))
    print('\033[1:33mBoa compra e aproveite seu imóvel!\033[m')
