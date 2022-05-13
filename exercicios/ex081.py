valores = []
cont = 0
while True:
    num = valores.append(int(input('Digite um valor: ')))
    cont += 1
    resposta = input('Quer continuar? [S/N] ').upper().strip()
    if resposta == 'N':
        break
valores.sort(reverse = True)
print(f'Você digitou {cont} elementos')
print(f'Os valores em ordem decrescente são: {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não se encontra na lista!')
