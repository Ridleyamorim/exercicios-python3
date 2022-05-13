soma = 0
num = int(input('Digite um número: '))
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[33m', end= '')
        soma += 1
    else:
        print('\033[31m', end= '')
    print(i, end = " ")
print(f'\nO número {num} foi divisível {soma} vezes')
if soma > 2:
    print('E por isso ele NÃO É um número primo!')
else:
    print('E por isso ele É um número primo!')