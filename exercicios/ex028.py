import random
print('-=-'*25)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*25)
n = int(*input('Em que número eu pensei? '))
print('PROCESSANDO...')
sorteado = random.randrange(0, 5)
if sorteado == n:
    print('PARABÉNS! Você é um vidente!')
else:
    print('Infelizmente não foi dessa vez champz...')