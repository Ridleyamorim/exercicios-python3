from random import randint
from time import sleep
from operator import itemgetter
jogos = dict()
pos = list()
print('Valores sorteados:')
for c in range(0, 4):  
    jogos[f'Jogador{c+1}'] = randint(1, 6)
for k, v in jogos.items():
    sleep(1)
    print(f'{k} tirou {v} no dado.')
pos = sorted(jogos.items(), key=itemgetter(1), reverse=True) #ordenou o dicionario em ordem decrescente. itemgetter(1) busca o value do dict. se fosse itemgetter(0) iria buscar o key.
print('-=' * 30)
print('  ==',f'{"RANKING DOS JOGADORES":^2}','==')
for i, v in enumerate(pos): #for nesse formato porque pos é uma lista!
    print(f'    {i+1}º lugar: {v[0]} com: {v[1]}')
    sleep(1)
