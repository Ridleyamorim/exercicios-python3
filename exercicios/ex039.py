import datetime
sexo = input('Informe o seu sexo: ').strip().lower()
ano = int(input('Ano de nascimento: '))
presente = datetime.date.today().year
idade = presente - ano
print('Quem nasceu em {}, e possui {} anos em {}.'.format(ano, idade, presente))
if sexo == 'feminino':
    print('Você não precisa se alistar, a obrigatoriedade é apenas para o sexo MASCULINO.')
elif idade < 18:
    print('Ainda faltam {} anos para o alistamento'.format(18 - idade))
    print('Seu alistamento será em {}'.format(ano + 18))
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))
    print('Seu alistamento foi em {}'.format(ano + 18))
elif idade == 18:
    print('Você precisa se alistar IMEDIATAMENTE, para não ter perda de direitos!')
