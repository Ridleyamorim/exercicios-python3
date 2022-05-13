geral = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        geral[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 40)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{geral[l][c]:^5}]', end='')
    print()

    