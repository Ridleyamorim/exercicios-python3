dist = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.0f}km.'.format(dist))
if dist <= 200:
    gas = dist * 0.5
else:
    gas = dist * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(gas))