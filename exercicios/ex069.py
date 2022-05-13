adultos = homens = mulheres = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').upper().strip()[0]
    print('-' * 20)
    if idade > 18:
        adultos += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').upper().strip()[0]
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {adultos}\nAo todo temos {homens} homens cadastrados.\nE temos {mulheres} mulheres com menos de 20 anos.')


