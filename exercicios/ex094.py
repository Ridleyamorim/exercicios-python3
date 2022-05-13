geral= []
dados = {}
cont = soma = 0
sexo = ''
while True:
    dados['nome'] = input('Nome: ')
    sexo = input('Sexo [M/F]: ').upper().strip()
    dados['sexo'] = sexo    
    idade = int(input('Idade: '))
    dados['idade'] = idade
    resp = input('Quer continuar? [S/N] ').upper().strip()
    dados['cod'] = cont
    geral.append(dados.copy())
    dados.clear()
    soma += idade
    cont += 1
    if resp == 'N':
        break
media = soma / cont
print(f'A)  Ao todo temos {cont} pessoas cadastradas.')
print(f'B)  A média de idade é de {media:.1f} anos')
print(f'C)  As mulheres cadastradas foram: ', end='')
for c in geral:
    if c['sexo'] == 'F':
        print(c['nome'], end=' ')
print('\nD)   As pessoas que estão acima da média:')
for c in geral:
    if c['idade'] > media:
        print('     ', end='')
        for k, v in c.items():
            print(f'{k} = {v}; ', end='')
    print()
print('<<< ENCERRADO >>>')
