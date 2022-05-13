soma = 0
for c in range (0, 7):
    number = int(input('Set your number: '))
    if number % 2 == 0:
        soma += number
print('A soma dos números pares foi de {}'.format(soma)) 