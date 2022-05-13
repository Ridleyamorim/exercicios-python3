print('-' * 50)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('-' * 50)
listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livros', 34.90)
for c in range(0, len(listagem), 2):
    itens = listagem[c]
    preços = listagem[c + 1]
    print(f'{itens:.<40} R$ {preços:>6.2f}')
print('-' * 50)