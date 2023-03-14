from datetime import date
ano = int(input('Insira o ano de nascimento do atleta: '))
idade = date.today().year - ano
categoria = ''
if idade <= 9:
    categoria = '\033[35mMIRIM\033[m'
elif idade <= 14:
    categoria = '\033[32mINFANTIL\033[m'
elif idade <= 19:
    categoria = '\033[33mJÚNIOR\033[m'
elif idade <= 20:
    categoria = '\033[36mSÊNIOR\033[m'
else:
    categoria = '\033[31mMASTER\033[m'
print('O atleta tem {} anos e sua categoria é {}'.format(idade, categoria))
