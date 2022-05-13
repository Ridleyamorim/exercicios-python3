import datetime
niver = int(input('Ano de nascimento: '))
atual = datetime.date.today().year
idade = atual - niver
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14: 
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificalção: SÊNIOR')
else: 
    print('Classificação: MASTER')