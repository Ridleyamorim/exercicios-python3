frase = input('Digite uma frase: ').strip().lower()
print('A letra A aparece {} vezes na frase'.format(frase.count('a')))
print('A primeira vez que A apareceu foi na posição {}'.format(frase.find('a')))
print('A última letra A apareceu na posição {}'.format(frase.rfind('a')))