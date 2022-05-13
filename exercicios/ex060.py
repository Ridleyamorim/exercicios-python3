n = int(input('Digite um número para calcular seu Fatorial: '))
fatorial = n 
produto = 1
print(f'Calculando {n}! = ', end='')
while fatorial > 0:
    print(f'{fatorial}', end='')
    print(' x ' if fatorial > 1 else ' = ', end='')
    produto *= fatorial
    fatorial -= 1
print(produto)
    