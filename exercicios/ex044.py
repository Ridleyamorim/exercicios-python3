print('=' * 15 , 'LOJAS RIDLEY', '=' * 15)
compras = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO\n[1] à vista dinheiro/cheque\n[2] à vista cartão\n[3] 2x no cartão\n[4] 3x ou mais no cartão')
opção = int(input('Qual é a opção? '))
if opção == 1:
    novo = compras * 0.90
elif opção == 2:
    novo = compras * 0.95
elif opção == 3:
    novo = compras
elif opção == 4:
    novo = compras * 1.2
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(compras, novo))