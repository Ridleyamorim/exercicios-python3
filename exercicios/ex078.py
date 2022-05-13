valores = [int(input('Digite um valor para a Posição 0: ')), int(input('Digite um valor para a Posição 1: ')), int(input('Digite um valor para a Posição 2: ')), int(input('Digite um valor para a Posição 3: ')), int(input('Digite um valor para a Posição 4: '))]
print(f'Você digitou os valores: {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')
for c, v in enumerate(valores):
    if v == max(valores):
        print(c, end='...')
print(f'\nO menor valor digitado foi {min(valores)} nas posições ', end='')
for c, v in enumerate(valores):
    if v == min(valores):
        print(c, end='...')
