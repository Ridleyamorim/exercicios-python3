from random import randint
from time import sleep
geral = []
dados = []
num = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-=-= SORTEANDO {num} JOGOS -=-=-=-=')
for j in range(0, num):
    print(f'Jogo {j + 1}: ', end='')
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in dados:
            dados.append(num)
            cont += 1
        if cont >= 6:
            break
    geral.append(dados[:])
    dados.clear()
    print(geral[j])
    sleep(1)