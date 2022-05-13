def ficha(jog='<desconhecido>', gols=0):
    return f'{jog} fez {gols} gol(s) no campeonato.'


nomeJog = input('Nome do Jogador: ')
numGols = input('Número de gols: ')
'''if numGols.isnumeric():
    numGols = int(numGols)
else:
    numGols = 0
if nomeJog.strip() == ''  
    ficha(gols=numGols)
else:
    ficha(nomeJog, numGols)
# resposta do professor acima. Abaixo a minha.
'''
if nomeJog == '' and numGols == '':
    print(ficha())
elif nomeJog != '' and numGols != '':
    print(ficha(nomeJog, numGols))
elif nomeJog == '' and numGols != '':
    print(ficha(gols=numGols))
elif numGols == '' and nomeJog != '':
    print(ficha(nomeJog))

