valor = int(input('Digite um número para ver sua tabuada: '))
for c in range (1, 11):
    produto = c * valor
    print('{} x {} = {}'.format(valor, c, produto))