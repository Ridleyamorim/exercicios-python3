from datetime import datetime
geral = {}
cont = 0
while cont < 1:
    geral['nome'] = input('Nome: ')
    geral['idade'] = datetime.today().year - int(input('Ano de nascimento: '))
    geral['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
    if geral['ctps'] == 0:
        break
    else:
        geral['contratação'] = int(input('Ano de contratação: '))
        geral['salário'] = float(input('Salário: '))
        geral['aposentadoria'] = geral['contratação'] + 35 - datetime.today().year + geral['idade']
    cont += 1
print('-=' * 30)
for k, v in geral.items():
    if k == 'ctps' and v == 0:
        print('  - Não possui ctps!')
    else:
        print(f'  - {k} tem o valor {v}')