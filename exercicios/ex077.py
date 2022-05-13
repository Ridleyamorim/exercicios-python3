palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for c in range(0, len(palavras)):
    itens = palavras[c]
    print(f'\nNa palavra {itens} temos ', end='')
    for i in range(0, len(itens)):
        letras = itens[i]
        vogais = ''
        if letras in 'AEIOU':
            vogais += letras
        print(f'{vogais}', end='')