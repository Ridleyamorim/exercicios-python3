print('\033[0;31;40m-=-'*20)
print('Analisador  de triângulos')
print('-=-'*20)
a = float(input('Primeiro segmento:'))
b = float(input('Segundo segmento:'))
c = float(input('Terceiro segmento:'))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else: 
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')

