from math import hypot

oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))
hipo = hypot(oposto, adjacente)
print('A hipotenusa vai medir {:.2f}'.format(hipo))