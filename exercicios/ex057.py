#validação simples de dados
sexo = input('Informe seu sexo: [M/F] ').upper().strip()[0] # o index fará verificar apenas uma letra, mesmo que a pessoa digite nome inteiro
while sexo not in 'MmFf':
    sexo = input('Dados inválidos. Por favor, informe seu sexo corretamente: ').upper().strip()[0]
print(f'Sexo {sexo} registrado com sucesso!')

    