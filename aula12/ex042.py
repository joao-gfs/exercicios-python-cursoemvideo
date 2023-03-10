s1 = float(input('Digite o comprimento do primeiro segmento: '))
s2 = float(input('Digite o comprimento do segundo segmento: '))
s3 = float(input('Digite o comprimento do terceiro segmento: '))
if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    tipo = ''
    if s1 == s2 == s3:
        tipo = 'equilátero'
    elif s1 == s2 or s2 == s3 or s1 == s3:
        tipo = 'isósceles'
    else:
        tipo = 'escaleno'
    print('Esses segmentos podem formar um triângulo \033[1m{}\033[m!'.format(tipo))
else:
    print('Esses segmentos não podem formar um triângulo.')
