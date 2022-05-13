import random
attempts = 1
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10')
print('Será que você consegue adivinhar qual foi?')
pc = random.randint(0, 10)
guess = int(input('Qual o seu palpite? '))
if guess > 10 or guess < 0:
    print('Favor inserir um número válido.')
    guess = int(input('Qual o seu palpite? '))
else:
    while pc != guess:
        if pc > guess:
            print('Menos... Tente mais uma vez')
            guess = int(input('Qual o seu palpite? '))
        else:
            print('Mais... Tente mais uma vez')
            guess = int(input('Qual o seu palpite? '))
        attempts += 1
print(f'Acertou com {attempts} tentativas. Parabéns!')
