geral = list()
dados = dict()
partidas = list()
while True:
    dados.clear()
    dados['nome'] = input('Nome do Jogador: ')
    num = int(input(f'Quantas partidas {dados["nome"]} jogou: '))
    for i in range(0, num):
        gols = int(input(f'   Quantos gols na partida {i+1}? '))
        partidas.append(gols)
    dados['gols'] = partidas.copy()
    dados['total'] = sum(partidas)
    partidas.clear()
    geral.append(dados.copy())
    resp = input('Quer continuar? [S/N] ').upper().strip()[0]
    if resp == 'N':
        break
print('-=' * 40)
print('cod  ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(geral):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    print('-' * 40)
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break  
    if  busca >= len(geral):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {geral[busca]["nome"]}:')
        for i, c in enumerate(geral[busca]["gols"]):
            print(f'     No jogo {i + 1}, fez {c} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')

