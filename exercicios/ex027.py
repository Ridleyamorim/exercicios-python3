name = input('Digite seu nome completo: ').strip()
print('Muito prazer em te conhecer! ')
print('Seu primeiro nome é {}'.format(name[:name.find(' ')]))
print('Seu último nome é {}'.format(name[name.rfind(' '):]))