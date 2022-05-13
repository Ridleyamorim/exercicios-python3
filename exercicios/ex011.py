largura = float(input('Largura  da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
tinta = area / 2
print('Sua parede tem a dimensão de {} x {} e sua área é de {:.3f}m².\nPara pintar essa parede, você precisará de {:.4f}l de tinta.'.format(largura, altura, area, tinta))