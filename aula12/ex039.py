from datetime import date
ano = int(input('Insira seu ano de nascimento para ter informações sobre o alistamento obrigatório: '))
idade = date.today().year - ano
if idade == 17:
    print('\033[4;32mVocê fará 18 anos ano que vem, então está na hora de se alistar!\033[m')
elif idade < 17:
    print('\033[4;34mVocê ainda vai se alistar! Faltam {} anos para seu alistamento.\033[m'.format(17 - idade))
else:
    print('\033[4;31mVocê deveria ter se alistado há {} anos! Compareça ao quartel para se regularizar.\033[m'.format(idade - 17))
