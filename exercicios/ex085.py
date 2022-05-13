geral = []
pares = []
impares = []
for c in range(0, 7):
    num = int(input(f'Digite o {c + 1}º valor: '))
    if num % 2 == 0:
        pares.append(num)  
    else:
        impares.append(num) 
pares.sort()
impares.sort()      
geral.append(pares[:])
geral.append(impares[:])
print(f'Os valores pares digitados foram: {geral[0]}')
print(f'Os valores pares digitados foram: {geral[1]}')