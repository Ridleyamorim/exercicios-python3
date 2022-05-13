from time import sleep
geral = []
dados = []
notas = []
cont = 0
while True:
    nome = dados.append(input('Nome: '))
    nota1 = notas.append(float(input('Nota 1: ')))
    nota2 = notas.append(float(input('Nota 2: ')))
    dados.append(notas[:]) #alternativa de resposta: media = (nota1+nota2)/2  | geral.append([nome, [nota1, nota2], media])
    geral.append(dados[:])
    notas.clear()
    dados.clear()
    resp = input('Quer continuar? [S/N] ').upper().strip()
    cont += 1
    if resp == 'N':
        break
print('-=' * 40)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 25)
sleep(1)
for i in range (0, cont): # alternativa:  for i, a in enumerate(geral) ---> com isso geral[i][0] poderia ser a[0]
    print(f'{i:<4}', end='')
    print(f'{geral[i][0]:<10}', end='')
    print(f'{(geral[i][1][0] + geral[i][1][1]) / 2:>8.2f}')
sleep(1)
while True:
    print('-' * 30)
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if mostrar == 999:
        break
    if mostrar <= len(geral) - 1:
        print(f'As notas de {geral[mostrar][0]} são {geral[mostrar][1]}')
sleep(1)
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
