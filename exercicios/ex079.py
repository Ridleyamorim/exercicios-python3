valores = list()
while True:
    num = int(input('Digite um valor: '))  
    if num in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        print('Valor adicionado com sucesso...')
        valores.append(num)
    escolha = input('Quer continua? [S/N] ').upper().strip()
    if escolha == 'N':
        break
print('-=-' * 40)
valores.sort()
print(f'Você digitou os valores {valores}')
    