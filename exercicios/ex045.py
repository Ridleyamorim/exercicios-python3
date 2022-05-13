import random
print(''' Suas escolhas:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
escolha = int(input('Qual a sua jogada? '))
pc = random.randrange()
if escolha == pc:
    print('EMPATE, os dois escolheram {}'.format(escolha))
print(pc)