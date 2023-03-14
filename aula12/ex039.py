from datetime import date
ano = int(input('Insira seu ano de nascimento para ter informações sobre o alistamento obrigatório: '))
idade = date.today().year - ano
if idade == 18:
    print('\033[4;32mVocê fará 18 anos ano que vem, então está na hora de se alistar!\033[m')
elif idade < 18:
    print('\033[4;34mVocê ainda vai se alistar! Faltam {} anos para seu alistamento.\033[m'.format(18 - idade))
    print('\033[4;34mSeu alistamento será em {}.\033[m'.format(ano + 18))
else:
    print('\033[4;31mVocê deveria ter se alistado há {} anos! Compareça ao quartel para se regularizar.\033[m'.format(idade - 18))
    print('\033[4;31mO alistamento deveria ter acontecido em {}.\033[m'.format(ano + 18))
