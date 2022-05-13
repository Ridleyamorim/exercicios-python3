num1 = int(input('Digite um número: '))
num2 = int(input('Digite mais um número: '))
num3 = int(input('Digite outro número: '))
num4 = int(input('Digite o último número: '))
tupla = (num1, num2, num3, num4)
cont = 0
for c in range(0, len(tupla)):
    valores = tupla[c]
    if valores % 2 == 0:
        cont += 1
print(tupla)
print('O número 9 apareceu {} vezes'.format(tupla.count(9)))
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}ª posição')
else: 
    print('O valor 3 não foi digitado em nenhuma posição!')
print(f'Os valores pares digitados foram {cont}.')
