dis = float(input('Digite a distância em km da viagem: '))
if dis <= 200:
    print('Para uma viagem de {:.2f}, o valor será de R${:.2f}'.format(dis, dis*0.5))
else:
    print('Para uma viagem de {:.2f}, o valor será de R${:.2f}'.format(dis, dis*0.45))
