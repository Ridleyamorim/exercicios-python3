smaller = 0
bigger = 0
for i in range (1, 6):
    weight = float(input(f'Peso da {i}ª pessoa: '))
    if i == 1:
        bigger = weight
        smaller = weight
    else:
        if weight > bigger:
            bigger = weight
        if weight < smaller:
            smaller = weight
print(f'O maior peso lido foi de {bigger}Kg')
print(f'O menor peso lido foi de {smaller}Kg')