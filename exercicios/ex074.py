from random import randint
um = randint(1, 10)
dois = randint(1, 10)
três = randint(1, 10)
quatro = randint(1, 10)
cinco = randint(1, 10)
sorteados = (um, dois, três, quatro, cinco)
maior = menor = 0
for c in range(0, len(sorteados)):
    item = sorteados[c]
    if c == 1:
        maior = item
        menor = item
    if item > maior:
        maior = item
    elif item < menor:
        menor = item
# MANEIRA MAIS SIMPLES:
# print(f'O maior valor sorteado foi {max(sorteados)}')
# print(f'O menor valor sorteado foi {min(sorteados)}')
print(sorteados)
print(f'O menor  valor sorteado foi {menor}')
print(f'O maior valor sorteado foi {maior}')
