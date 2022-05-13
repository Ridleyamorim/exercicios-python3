frase = input('Digite uma frase: ').upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
valor = junto
contrario = ''
for valor in range (len(junto) - 1, -1, -1):
    contrario += junto[valor]
print(contrario, end='')
if junto == contrario:
    print('\nTemos um palíndromo!')
else:
    print('\nNão é um palíndromo!')