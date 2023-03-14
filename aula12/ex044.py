print(f'{" LOJÃO DO JOÃO ":=^40}')
valor = float(input('Valor do produto: R$'))
print('''Escolha a forma de pagamento:
1 - À vista no dinheiro/pix: 10% de desconto.
2 - À vista no cartão: 5% de desconto.
3 - Em 2x no cartão.
4 - Em 3x ou mais no cartão: 20% de juros.''')
forma = int(input(''))
if forma == 1:
    print('Você escolheu o pagamento à vista no dinheiro/pix.')
    print('O valor a ser pago será R${:.2f}'.format(valor * 0.9))
elif forma == 2:
    print('Você escolheu o pagamento à vista no cartão.')
    print('O valor a ser pago será R${:.2f}'.format(valor * 0.95))
elif forma == 3:
    print('Você escolheu o pagamento parcelado em 2x no cartão.')
    print('O valor das parcelas será de R${:.2f}, totalizando R${:.2f} a serem pagos.'.format(valor/2, valor))
elif forma == 4:
    print('Você escolheu o pagamento parcelado em 3x ou mais. Favor digite em quantas vezes deseja parcelar: ')
    parcela = int(input(''))
    if parcela < 3:
        print('Neste caso, escolha outra forma de pagamento para ter um preço melhor.')
    else:
        print('Parcelando em {}x, cada parcela custará R${:.2f}, totalizando R${:.2f}.'.format(parcela, valor * 1.2 / parcela, valor * 1.2))
else:
    print('Favor escolher uma das 4 opções de pagamento.')
