geral = []
dados = []
menor = maior = cont = 0
while True:
    nome = dados.append(input('Nome: '))
    idade = dados.append(float(input('Peso (Kg): ')))   
    if len(geral) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    geral.append(dados[:])
    dados.clear()
    cont += 1             
    resp = input('Deseja continuar? [S/N] ').upper().strip()
    if resp == 'N':
        break
print('-=' * 40)
print(f'Ao todo, você cadastrou {cont} pessoas')
print (f'O maior peso foi de {maior} Kg. Peso de ', end='')
for p in geral:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print (f'\nO menor peso foi de {menor} Kg. Peso de ', end='')
for p in geral:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
