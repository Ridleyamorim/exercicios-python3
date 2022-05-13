valores = []
pares = []
impares = []
while True:
    num = valores.append(int(input('Digite um número: ')))
    resp = input('Quer continuar? [S/N] ').upper().strip()
    if resp == 'N':
        break
print(f'A lista completa é: {valores}')
for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'A lista de pares é: {pares}')
print(f'A lista de ímpares é: {impares}')