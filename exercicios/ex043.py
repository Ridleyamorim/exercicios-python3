p = float(input('Qual o seu peso? '))
h = float(input('Qual a sua altura? '))
imc = p / pow(h , 2) 
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso ideal')
elif imc < 25:
    print('Você está no peso IDEAL!')
elif imc <= 30:
    print('Você está com SOBREPESO!')
elif imc <= 40:
    print('Você está OBESO!')
else:
    print('Você está com OBESIDADE MÓRBIDA!')
