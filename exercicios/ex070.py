cont = total = totMil = menor = 0
barato =''
while True:
    print('-' * 20)
    print('LOJA SUPER BARATÃO')
    print('-' * 20)
    produto = input('Nome do Produto: ').strip().upper()[0]
    preço = float(input('Preço: '))
    cont += 1
    total += preço
    if produto > 1000:
        totMil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totMil} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')