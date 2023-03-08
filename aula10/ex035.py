s1 = float(input('Digite o comprimento do primeiro segmento: '))
s2 = float(input('Digite o comprimento do segundo segmento: '))
s3 = float(input('Digite o comprimento do terceiro segmento: '))
if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    print('Esses segmentos podem formar um triângulo.')
else:
    print('Esses segmentos não podem formar um triângulo.')
