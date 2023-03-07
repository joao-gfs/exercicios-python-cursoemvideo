l1 = float(input('Digite o comprimento da primeira reta: '))
l2 = float(input('Digite o comprimento da segunda reta: '))
l3 = float(input('Digite o comprimento da terceira reta: '))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('Essas retas podem formar um triângulo.')
else:
    print('Essas retas não podem formar um triângulo.')
