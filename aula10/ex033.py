a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))

if a > b:
    if a > c:
        if b > c:
            print('O maior é {} e o menor é {}'.format(a, c))
        else:
            print('O maior é {} e o menor é {}'.format(a, b))
    else:
        print('O maior é {} e o menor é {}'.format(c, b))
elif b > c:
    if c > a:
        print('O maior é {} e o menor é {}'.format(b, a))
    else:
        print('O maior é {} e o menor é {}'.format(b, c))
else:
    print('O maior é {} e o menor é {}'.format(c, a))
