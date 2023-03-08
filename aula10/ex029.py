vel = float(input('Qual a velocidade do carro? '))
if vel > 80:
    print('Você ultrapassou o limite de velocidade e foi multado.\nO valor total da multa é de R${:.2f}'.format((vel-80)*7))
else:
    print('Você está dentro dos limites de velocidade. Boa viagem!')
