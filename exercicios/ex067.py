# TABUADA
while True:
    print('-' * 30)
    valor = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if valor < 0:
        break
    for c in range(1, 11):
        produto = valor * c
        print (f'{valor} x {c} = {produto}')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre, amigo(a).')

