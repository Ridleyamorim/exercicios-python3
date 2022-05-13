dados = dict()
partidas = list()
soma = 0
dados['nome'] = input('Nome do Jogador: ')
num = int(input(f'Quantas partidas {dados["nome"]} jogou: '))
for i in range(0, num):
    gols = int(input(f'   Quantos gols na partida {i}? '))
    soma += gols
    partidas.append(gols)
dados['gols'] = partidas.copy()
dados['total'] = soma
print('-=' * 40)
print(dados)
print('-=' * 40)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 40)
print(f'O jogador {dados["nome"]} jogou {num} partidas.')
for i, c in enumerate(partidas):
    print(f'    => Na partida {i}, fez {c} gols.')
print(f'Foi um total de {soma} gols.')