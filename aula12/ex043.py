peso = float(input('Insira seu peso em quilos: '))
altura = float(input('Insira sua altura em metros: '))
imc = peso / altura ** 2
status = ''
if imc <= 18.5:
    status = '\033[33mabaixo do peso\033[m'
elif imc <= 25:
    status = '\033[32mno peso ideal\033[m'
elif imc <= 30:
    status = '\033[33mcom sobrepeso\033[m'
elif imc <= 40:
    status = '\033[31mobeso(a)\033[m'
else:
    status = '\033[4;31mcom obesidade mórbida\033[m'
print('O seu IMC é de {:.2f}, o que indica que você está {}.'.format(imc, status))
