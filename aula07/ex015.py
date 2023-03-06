pdias = float(input('Quantos dias alugados? ')) * 60
pkm = float(input('Quantos Km rodados? ')) * 0.15
print('O total a pagar é de R${:.2f}'.format(pdias + pkm))
