prim = int(input('Primeiro número: '))
seg = int(input('Segundo número: '))
resultado = prim - seg
if resultado > 0:
    print('O PRIMEIRO valor é maior')
elif resultado < 0:
    print('O SEGUNDO valor é maior')
elif resultado == 0:
    print('Não existe valor maior, os dois sãqo iguais')