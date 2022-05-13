geral = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = col3 = maior = 0
for l in range(0, 3):
    for c in range(0, 3): #usar while true pode ser uma melhor opção. Coloca if <= 6 /break e cont+= 1 no 3º if 
        num = int(input(f'Digite um valor para [{l}, {c}]: '))
        geral[l][c] = num
        if num % 2 == 0:
            pares += num
        if c == 2:
            col3 += num
        if l == 1 and c == 0:
            maior = menor = num
        elif l == 1:
            if num > maior:
                maior = num
print('-=' * 40)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{geral[l][c]:^5}]', end='')
    print()
print('-=' * 40)
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {col3}')
print(f'O maior valor da segunda linha é de {maior}')
