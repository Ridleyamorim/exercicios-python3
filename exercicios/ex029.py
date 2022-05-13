velocity = int(input('Qual é a velocidade atual do carro? '))
if velocity > 80:
    print('MULTADO! Você excedeu o limnite permitido que é de 80km/h.')
    multa = velocity * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
    
print('Tenha um bom dia! Dirija com segurança!')
